#include "mutable/util/macro.hpp"
#include <mutable/IR/Optimizer.hpp>

#include <algorithm>
#include <mutable/catalog/Catalog.hpp>
#include <mutable/IR/Operator.hpp>
#include <mutable/Options.hpp>
#include <mutable/parse/AST.hpp>
#include <mutable/storage/Store.hpp>
#include <numeric>
#include <tuple>
#include <vector>
#include <queue>
#include <unordered_set>


using namespace m;
using namespace m::ast;


/*======================================================================================================================
 * Helper functions
 *====================================================================================================================*/

struct WeighExpr
{
    private:
    unsigned weight_ = 0;

    public:
    operator unsigned() const { return weight_; }

    void operator()(const cnf::CNF &cnf) {
        for (auto &clause : cnf)
            (*this)(clause);
    }

    void operator()(const cnf::Clause &clause) {
        for (auto pred : clause)
            (*this)(*pred);
    }

    void operator()(const ast::Expr &e) {
        visit(overloaded {
            [](const ErrorExpr&) { M_unreachable("no errors at this stage"); },
            [this](const Designator &d) {
                if (auto cs = cast<const CharacterSequence>(d.type()))
                    weight_ += cs->length;
                else
                    weight_ += 1;
            },
            [this](const Constant &e) {
                if (auto cs = cast<const CharacterSequence>(e.type()))
                    weight_ += cs->length;
                // fixed-size constants are considered free, as they may be encoded as immediate constants in the instr
            },
            [this](const FnApplicationExpr&) {
                weight_ += 1;
            },
            [this](const UnaryExpr&) { weight_ += 1; },
            [this](const BinaryExpr&) { weight_ += 1; },
            [this](const QueryExpr&) { weight_ += 1000; } // XXX: this should never happen because of unnesting
        }, e, tag<ConstPreOrderExprVisitor>{});
    }
};

std::vector<cnf::CNF> Optimizer::optimize_filter(cnf::CNF filter)
{
    constexpr unsigned MAX_WEIGHT = 12; // equals to 4 comparisons of fixed-length values
    M_insist(not filter.empty());

    /* Compute clause weights. */
    std::vector<unsigned> clause_weights;
    clause_weights.reserve(filter.size());
    for (auto &clause : filter) {
        WeighExpr W;
        W(clause);
        clause_weights.emplace_back(W);
    }

    /* Sort clauses by weight using an index vector. */
    std::vector<std::size_t> order(filter.size(), 0);
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&clause_weights](std::size_t first, std::size_t second) -> bool {
        return clause_weights[first] < clause_weights[second];
    });

    /* Dissect filter into sequence of filters. */
    std::vector<cnf::CNF> optimized_filters;
    unsigned current_weight = 0;
    cnf::CNF current_filter;
    for (std::size_t i = 0, end = filter.size(); i != end; ++i) {
        const std::size_t idx = order[i];
        cnf::Clause clause(std::move(filter[idx]));
        M_insist(not clause.empty());
        const unsigned clause_weight = clause_weights[idx];

        if (not current_filter.empty() and current_weight + clause_weight > MAX_WEIGHT) {
            optimized_filters.emplace_back(std::move(current_filter)); // empties current_filter
            current_weight = 0;
        }

        current_filter.emplace_back(std::move(clause));
        current_weight += clause_weight;
    }
    if (not current_filter.empty())
        optimized_filters.emplace_back(std::move(current_filter));

    M_insist(not optimized_filters.empty());
    return optimized_filters;
}

std::vector<Optimizer::projection_type>
Optimizer::compute_projections_required_for_order_by(const std::vector<projection_type> &projections,
                                                     const std::vector<order_type> &order_by)
{
    std::vector<Optimizer::projection_type> required_projections;

    /* Collect all required `Designator`s which are not included in the projection. */
    auto get_required_designator = overloaded {
        [&](const ast::Designator &d) -> void {
            if (auto t = std::get_if<const Expr*>(&d.target())) { // refers to another expression?
                /*----- Find `t` in projections. -----*/
                for (auto &[expr, _] : projections) {
                    if (*t == &expr.get())
                        return; // found
                }
            }
            /*----- Find `d` in projections. -----*/
            for (auto &[expr, alias] : projections) {
                if (not alias.has_value() and d == expr.get())
                    return; // found
            }
            required_projections.emplace_back(d, ThreadSafePooledOptionalString{});
        },
        [&](const ast::FnApplicationExpr &fn) -> void {
            /*----- Find `fn` in projections. -----*/
            for (auto &[expr, alias] : projections) {
                if (not alias.has_value() and fn == expr.get())
                    throw visit_skip_subtree(); // found
            }
            required_projections.emplace_back(fn, ThreadSafePooledOptionalString{});
            throw visit_skip_subtree();
        },
        [](auto&&) -> void { /* nothing to be done */ },
    };
    /* Process the ORDER BY clause. */
    for (auto [expr, _] : order_by)
        visit(get_required_designator, expr.get(), m::tag<m::ast::ConstPreOrderExprVisitor>());

    return required_projections;
}


/*======================================================================================================================
 * Optimizer_ResultDB
 *====================================================================================================================*/
/** Identifies a set of joins that have to be computed such that the join graph becomes acyclic. Currently, the
 * implementation heuristically chooses the node `x` with the highest degree first and subsequently, identifies the node
 * `y` with the highest degree from the neighbors of `x`. The rationale behind this is that nodes with a high degree are
 * more likely to be part of a cycle.
 *
 * TODO: Instead of repeatedly choosing two nodes heuristically and checking if the resulting graph is acyclic, we can
 * use Tarjans bridge-finding algorithm:
 * https://en.wikipedia.org/wiki/Bridge_%28graph_theory%29#Tarjan's_bridge-finding_algorithm
 * Using this, we can successively remove bridges (i.e. joins that are not part of a cycle) and with that, narrow down
 * the set of relations such that we know that the resulting nodes are part a cycle.
 * Note, the query graph could only have joins that are part of a cycle, i.e. the algorithm would not be able to remove
 * any edges. In this case, it might still matter which folds are computed.
 */
std::vector<Optimizer_ResultDB::fold_t> Optimizer_ResultDB::compute_folds(const QueryGraph &G) const
{
    M_insist(G.is_cyclic(), "join graph must be cyclic");
    M_insist(G.num_sources() > 2, "join graph with two or less data sources cannot be cyclic");

    /*----- Get the ids of the data sources in `G` and put them in individual sets. -----*/
    std::vector<fold_t> folds;
    for (auto &ds : G.sources())
        folds.push_back({ds->id()});

    /*----- Compute the folds of the query graph. -----*/
    AdjacencyMatrix mat(G.adjacency_matrix()); // copy the query graphs adjacency matrix
    do {
        /*----- Compute `x` and `y` using the adjacency matrix. -----*/
        std::size_t x_id = mat.highest_degree_node(SmallBitset::All(folds.size()));
        std::size_t y_id = mat.highest_degree_node(mat.neighbors(SmallBitset::Singleton(x_id)));
        if (y_id < x_id)
            std::swap(x_id, y_id); // `x_id` contains the smaller id

        /*----- Merge the two folds. -----*/
        folds[x_id].merge(folds[y_id]);
        folds.erase(folds.begin() + y_id);

        mat = mat.merge_nodes(x_id, y_id); // merge the two nodes of the adjacency matrix
    } while (mat.is_cyclic());

    return folds;
}


/** Modify the `QueryGraph` based on the folds. Concretely, the data sources that are part of a fold are put together in
 * a (nested) query and the joins are adapted accordingly. */
void Optimizer_ResultDB::fold_query_graph(QueryGraph &G, std::vector<fold_t> &folds) const
{
    auto &C = Catalog::Get();

    /* Retrieve and reset data sources and joins in `G`. */
    const auto joins = std::exchange(G.joins(), std::vector<std::unique_ptr<Join>>());
    const auto sources = std::exchange(G.sources(), std::vector<std::unique_ptr<DataSource>>());

    /* Create a new `BaseTable` or `Query` with the same information as the data source at position `ds_id_in_G` in
     * `sources` and add it to the query graph `G`. Returns the id of the newly inserted data source. */
    auto add_ds_to_query_graph = [&sources](QueryGraph &G, std::size_t ds_id_in_G) -> std::size_t {
        auto &ds = sources[ds_id_in_G];
        auto new_id = G.sources().size();
        if (auto bt = cast<BaseTable>(ds.get())) {
            auto &new_bt = G.add_source(bt->name(), bt->table());
            new_bt.update_filter(std::move(bt->filter()));
        } else {
            auto &Q = as<Query>(*ds);
            auto &new_Q = G.add_source(Q.name(), Q.extract_query_graph());
            new_Q.update_filter(std::move(Q.filter()));
        }
        return new_id;
    };

    /* The `mod_nested_id` data structure stores the following information:
     *      (data source id in modified `G`, data source id in `G_nested` of modified `G`)
     * The index into the array corresponds to the id of the original data source in `G`.
     * The second value does not hold any meaning for base tables. */
    std::pair<std::size_t, std::size_t> ds2mod_nested_id[sources.size()];
    /*----- Create new data sources for the modified query graph. -----*/
    for (auto fold : folds) {
        if (fold.size() == 1) { // base table
            auto id = *fold.begin();
            auto ds_id = add_ds_to_query_graph(G, id);
            ds2mod_nested_id[id] = std::make_pair(ds_id, 0);
        } else { // nested query
            /*----- Create new `QueryGraph` and add as `DataSource` to `G`. -----*/
            auto G_nested = std::make_unique<QueryGraph>();
            G_nested->transaction(G.transaction()); // nested query requires same transaction ID
            auto ds_id_in_G_mod = G.sources().size();
            std::ostringstream oss;
            oss << '$';
            std::size_t count = 0;
            for (auto ds_id_in_G : fold) { // add data sources
                if (count != 0)
                    oss << '_';
                oss << sources[ds_id_in_G]->name();
                auto ds_id_in_G_nested = add_ds_to_query_graph(*G_nested, ds_id_in_G);
                ds2mod_nested_id[ds_id_in_G] = std::make_pair(ds_id_in_G_mod, ds_id_in_G_nested);
                ++count;
            }
            G.add_source(C.pool(oss.str().c_str()), std::move(G_nested));
        }
    }

    /*----- Create joins between the new data sources in `G`. -----*/
    for (auto &join : joins) {
        M_insist(join->sources().size() == 2);
        /*----- Create new `Join` and add to corresponding data source. -----*/
        auto G_lhs_id = join->sources()[0].get().id();
        auto G_rhs_id = join->sources()[1].get().id();

        auto [mod_lhs_id, nested_lhs_id] = ds2mod_nested_id[G_lhs_id];
        auto [mod_rhs_id, nested_rhs_id] = ds2mod_nested_id[G_rhs_id];
        auto &mod_lhs_ds = *G.sources()[mod_lhs_id];
        auto &mod_rhs_ds = *G.sources()[mod_rhs_id];

        auto add_join = [&join](QueryGraph &G, DataSource &lhs_ds, DataSource &rhs_ds) {
            /*----- Create new joins sources. -----*/
            Join::sources_t new_join_sources;
            new_join_sources.push_back(lhs_ds);
            new_join_sources.push_back(rhs_ds);

            /*----- Construct new join and add to `G`. -----*/
            auto &new_join = G.emplace_join(std::move(join->condition()), std::move(new_join_sources));

            /*----- Add new join to its respective data sources. -----*/
            lhs_ds.add_join(new_join);
            rhs_ds.add_join(new_join);
        };

        if (mod_lhs_id == mod_rhs_id) { // both data sources have the same `id` in `G` -> join inside nested query
            auto &Q_nested = as<Query>(mod_lhs_ds);
            auto &G_nested = Q_nested.query_graph();

            auto &nested_lhs = *G_nested.sources()[nested_lhs_id];
            auto &nested_rhs = *G_nested.sources()[nested_rhs_id];
            Join::sources_t nested_sources;
            nested_sources.push_back(nested_lhs);
            nested_sources.push_back(nested_rhs);
            add_join(G_nested, nested_lhs, nested_rhs);
            continue;
        }

        /*----- Check if this join already exists in `G`. -----*/
        auto it = std::find_if(G.joins().begin(), G.joins().end(), [&mod_lhs_ds, &mod_rhs_ds](auto &j){
            M_insist(j->sources().size() == 2);
            return (j->sources()[0].get() == mod_lhs_ds and j->sources()[1].get() == mod_rhs_ds) or
                   (j->sources()[1].get() == mod_lhs_ds and j->sources()[0].get() == mod_rhs_ds);
        });

        if (it != G.joins().end()) // already in `G` -> update condition
            (*it)->update_condition(std::move(join->condition()));
        else // construct new join and add to `G`
            add_join(G, mod_lhs_ds, mod_rhs_ds);
    }
}

/** If the `QueryGraph` contains multiple joins between two specific data sources, combine them into *one* join that
 * concatenates the individual conditions using a logical AND operation. */
void Optimizer_ResultDB::combine_joins(QueryGraph &G) const
{
    std::vector<std::unique_ptr<Join>> modified_joins;
    for (auto &j : G.joins()) {
        auto it = std::find_if(modified_joins.cbegin(), modified_joins.cend(), [&j](auto &mod_j){
            M_insist(j->sources().size() == 2);
            M_insist(mod_j->sources().size() == 2);
            return (j->sources()[0].get() == mod_j->sources()[0] and j->sources()[1].get() == mod_j->sources()[1]) or
                   (j->sources()[1].get() == mod_j->sources()[0] and j->sources()[0].get() == mod_j->sources()[1]);
        });
        if (it != modified_joins.cend())
            (*it)->update_condition(j->condition()); // `j` is already in `modified_joins` -> update condition
        else
            modified_joins.push_back(std::move(j)); // `j` is not in `modified_joins` -> add
    }
    G.joins() = std::move(modified_joins);
}

/** Chooses a root node that is part of the SELECT clause, i.e. appears in the projections. If there are multiple nodes,
 * choose the one with the highest degree. */
DataSource & Optimizer_ResultDB::choose_root_node(QueryGraph &G, SemiJoinReductionOperator &op) const
{
    const Schema &S = op.schema();
    std::size_t current_root_idx = -1UL;
    for (std::size_t idx = 0; idx < G.sources().size(); ++idx) {
        auto intersection = S & op.child(idx)->schema();
        if (not intersection.empty()) { // contained in projections
            if (current_root_idx == -1UL or (G.sources()[idx]->joins().size() > G.sources()[current_root_idx]->joins().size()))
                current_root_idx = idx;
        }
    }
    if (current_root_idx == -1UL) { // no relation found that is part of the projections (likely SELECT *)
        current_root_idx = 0;
        for (std::size_t idx = 1; idx < G.sources().size(); ++idx) { // fallback to highest degree
            if (G.sources()[idx]->joins().size() > G.sources()[current_root_idx]->joins().size())
                current_root_idx = idx;
        }
    }
    return *G.sources()[current_root_idx];
}

void Optimizer_ResultDB::compute_semi_join_reduction_order(QueryGraph &G, SemiJoinReductionOperator &op) const
{
    std::vector<semi_join_order_t> semi_join_reduction_order;

    /*----- Choose root node that is part of the projections and has the highest degree. -----*/
    auto &root = choose_root_node(G, op);

    /*----- Compute BFS ordering starting at `root`. -----*/
    auto &mat = G.adjacency_matrix();
    std::unordered_set<std::reference_wrapper<DataSource>, DataSourceHash, DataSourceEqualTo> visited;
    std::queue<std::reference_wrapper<DataSource>> Q;
    std::vector<std::reference_wrapper<DataSource>> BFS_ordering;
    Q.push(root);

    while (not Q.empty()) {
        auto x = Q.front();
        Q.pop();
        BFS_ordering.push_back(x);
        visited.insert(x);
        auto neighbors = mat.neighbors(SmallBitset::Singleton(x.get().id()));
        for (auto n_id : neighbors) {
            auto &n = *G.sources()[n_id];
            if (visited.contains(n))
                continue;
            Q.push(n);
        }
    }

    /*----- Use the BFS ordering of the data sources to construct the order in which the semi-joins are applied. -----*/
    std::unordered_set<std::reference_wrapper<Join>, JoinHash, JoinEqualTo> handled_joins;
    for (auto ds : BFS_ordering) {
        for (auto j : ds.get().joins()) {
            if (not handled_joins.contains(j)) {
                /*----- Check which join source (lhs or rhs) contains the current `ds` (closer to the root). -----*/
                using ds_it_t = decltype(j.get().sources().begin());
                auto [lhs, rhs] = [&j, &ds]() -> std::pair<ds_it_t, ds_it_t> {
                    M_insist(j.get().sources().size() == 2);
                    auto lhs = j.get().sources().begin();
                    auto rhs = std::next(lhs);
                    if (lhs->get() == ds.get())
                        return { lhs, rhs };
                    else
                        return { rhs, lhs };
                }();
                semi_join_reduction_order.emplace_back(*lhs, *rhs);
                handled_joins.insert(j);
            }
        }
    }
    op.semi_join_reduction_order() = std::move(semi_join_reduction_order);
}

std::pair<std::unique_ptr<Producer>, bool>
Optimizer_ResultDB::operator()(QueryGraph &G) const
{
    auto &C = Catalog::Get();
    auto &DB = C.get_database_in_use();
    auto &CE = DB.cardinality_estimator();

    /*----- Perform pre-optimizations on the QueryGraph. -----*/
    for (auto &pre_opt : C.pre_optimizations())
        (*pre_opt.second).operator()(G);

    if (G.sources().size() == 0)
        return { std::make_unique<ProjectionOperator>(G.projections()), false };

    /*----- Check that query graph is compatible. If not, report warning and fallback to standard `Optimizer`. -----*/
    if (G.sources().size() < 2 or
        not G.group_by().empty() or
        not G.aggregates().empty() or
        not G.order_by().empty() or
        G.limit().limit or
        G.limit().offset or
        std::any_of(G.joins().begin(), G.joins().end(), [](auto &join){ return not join->condition().is_equi(); }) or
        std::any_of(G.projections().begin(), G.projections().end(), [](auto &p){
            return not is<const ast::Designator>(p.first) or p.second.has_value(); // only designators without alias supported
        }))
    {
        std::cerr << "WARNING: No compatible query for ResultDB `Optimizer`. Fallback to standard `Optimizer`."
                  << std::endl;

        std::unique_ptr<Producer> producer;
        Optimizer Opt(C.plan_enumerator(), C.cost_function());
        producer = M_TIME_EXPR(Opt(G), "Compute the logical query plan", C.timer());
        return { std::move(producer), false };
    }

    /*----- Fold the query graph and compute semi-join reduction order. -----*/
    combine_joins(G); // in case there are multiple joins between two specific data sources
    if (G.is_cyclic()) {
        std::vector<fold_t> folds = compute_folds(G);
        fold_query_graph(G, folds);
    }

    /*----- Compute plans for data sources. -----*/
    const auto num_sources = G.sources().size();
    Producer **source_plans = new Producer*[num_sources];
    for (auto &ds : G.sources()) {
        Subproblem s = Subproblem::Singleton(ds->id());
        std::unique_ptr<DataModel> model;
        if (auto bt = cast<BaseTable>(ds.get())) {
            /* Produce a scan for base tables. */
            model = CE.estimate_scan(G, s);
            auto &store = bt->table().store();
            auto source = new ScanOperator(store, bt->name().assert_not_none());
            source_plans[ds->id()] = source;

            /* Set operator information. */
            auto source_info = std::make_unique<OperatorInformation>();
            source_info->subproblem = s;
            source_info->estimated_cardinality = CE.predict_cardinality(*model);
            source->info(std::move(source_info));
        } else {
            /* Recursively solve nested queries. */
            auto &Q = as<Query>(*ds);
            Optimizer Opt(C.plan_enumerator(), C.cost_function());
            auto [sub_plan, sub] = Opt.optimize(Q.query_graph());
            model = std::move(sub.model);

            /* If an alias for the nested query is given and the nested query was not introduced as a fold, i.e. it does
             * not start with '$', prefix every attribute with the alias. */
            if (Q.alias().has_value() and *Q.alias()[0] != '$') {
                M_insist(is<ProjectionOperator>(sub_plan), "only projection may rename attributes");
                Schema S;
                for (auto &e : sub_plan->schema())
                    S.add({ Q.alias(), e.id.name }, e.type, e.constraints);
                sub_plan->schema() = S;
            }

            /* Save the plan in the array of source plans. */
            source_plans[ds->id()] = sub_plan.release();
        }

        /* Apply filter, if any. */
        if (ds->filter().size()) {
            /* Update data model with filter. */
            auto new_model = CE.estimate_filter(G, *model, ds->filter());
            model = std::move(new_model);

            /* Optimize the filter by splitting into smaller filters and ordering them. */
            std::vector<cnf::CNF> filters = Optimizer::optimize_filter(ds->filter());
            Producer *filtered_ds = source_plans[ds->id()];

            /* Construct a plan as a sequence of filters. */
            for (auto &&filter : filters) {
                if (filter.size() == 1 and filter[0].size() > 1) { // disjunctive filter
                    auto tmp = std::make_unique<DisjunctiveFilterOperator>(std::move(filter));
                    tmp->add_child(filtered_ds);
                    filtered_ds = tmp.release();
                } else {
                    auto tmp = std::make_unique<FilterOperator>(std::move(filter));
                    tmp->add_child(filtered_ds);
                    filtered_ds = tmp.release();
                }
            }

            source_plans[ds->id()] = filtered_ds;
        }

        /* Set operator information. */
        auto source = source_plans[ds->id()];
        auto source_info = std::make_unique<OperatorInformation>();
        source_info->subproblem = s;
        source_info->estimated_cardinality = CE.predict_cardinality(*model); // includes filters, if any
        source->info(std::move(source_info));
    }

    /* Construct a semi join reduction operator with all necessary information requried by the code generation. */
    auto semi_join_reduction_op = std::make_unique<SemiJoinReductionOperator>(std::move(G.projections()));

    /* Add source plans as children. */
    for (std::size_t i = 0; i < num_sources; ++i)
        semi_join_reduction_op->add_child(source_plans[i]);

    compute_semi_join_reduction_order(G, *semi_join_reduction_op);
    semi_join_reduction_op->sources() = std::move(G.sources());
    semi_join_reduction_op->joins() = std::move(G.joins());

    delete[] source_plans;
    return { std::move(semi_join_reduction_op), true };
}


/*======================================================================================================================
 * Optimizer
 *====================================================================================================================*/

std::pair<std::unique_ptr<Producer>, PlanTableEntry> Optimizer::optimize(QueryGraph &G) const
{
    switch (Options::Get().plan_table_type)
    {
        case Options::PT_auto: {
            /* Select most suitable type of plan table depending on the query graph structure.
             * Currently a simple heuristic based on the number of data sources.
             * TODO: Consider join edges too.  Eventually consider #CSGs. */
            if (G.num_sources() <= 15) {
                auto [plan, PT] = optimize_with_plantable<PlanTableSmallOrDense>(G);
                return { std::move(plan), std::move(PT.get_final()) };
            } else {
                auto [plan, PT] = optimize_with_plantable<PlanTableLargeAndSparse>(G);
                return { std::move(plan), std::move(PT.get_final()) };
            }
        }

        case Options::PT_SmallOrDense: {
            auto [plan, PT] = optimize_with_plantable<PlanTableSmallOrDense>(G);
            return { std::move(plan), std::move(PT.get_final()) };
        }

        case Options::PT_LargeAndSparse: {
            auto [plan, PT] = optimize_with_plantable<PlanTableLargeAndSparse>(G);
            return { std::move(plan), std::move(PT.get_final()) };
        }
    }
}

template<typename PlanTable>
std::pair<std::unique_ptr<Producer>, PlanTable> Optimizer::optimize_with_plantable(QueryGraph &G) const
{
    PlanTable PT(G);
    const auto num_sources = G.sources().size();
    auto &C = Catalog::Get();
    auto &CE = C.get_database_in_use().cardinality_estimator();

    if (num_sources == 0) {
        PT.get_final().cost = 0; // no sources → no cost
        PT.get_final().model = CE.empty_model(); // XXX: should rather be 1 (single tuple) than empty
        return { std::make_unique<ProjectionOperator>(G.projections()), std::move(PT) };
    }

    /*----- Initialize plan table and compute plans for data sources. -----*/
    auto source_plans = optimize_source_plans(G, PT);

    /*----- Compute join order and construct plan containing all joins. -----*/
    optimize_join_order(G, PT);
    std::unique_ptr<Producer> plan = construct_join_order(G, PT, source_plans);
    auto &entry = PT.get_final();

    /*----- Construct plan for remaining operations. -----*/
    if (Options::Get().decompose) {
        /* Add `DecomposeOperator` on top of plan. */
        if (not G.group_by().empty() or
            not G.aggregates().empty() or
            not G.order_by().empty() or
            G.limit().limit or
            G.limit().offset or
            std::any_of(G.joins().begin(), G.joins().end(), [](auto &join){ return not join->condition().is_equi(); }) or
            std::any_of(G.projections().begin(), G.projections().end(), [](auto &p){
                return not is<const ast::Designator>(p.first) or p.second.has_value(); // only designators without alias supported
            }))
        {
            std::cerr << "WARNING: No compatible query to decompose. Fallback to standard `Optimizer`."
                      << std::endl;

            std::unique_ptr<Producer> producer;
            Optimizer Opt(C.plan_enumerator(), C.cost_function());
            producer = M_TIME_EXPR(Opt(G), "Compute the logical query plan", C.timer());
            return { std::move(producer), std::move(PT) };
        }
        auto decompose_op = std::make_unique<DecomposeOperator>(std::cout, std::move(G.projections()),
                                                                std::move(G.sources()));
        decompose_op->add_child(plan.release());
        plan = std::move(decompose_op);
    } else {
        plan = optimize_plan(G, std::move(plan), entry);
    }

    return { std::move(plan), std::move(PT) };
}

template<typename PlanTable>
std::unique_ptr<Producer*[]> Optimizer::optimize_source_plans(const QueryGraph &G, PlanTable &PT) const
{
    const auto num_sources = G.sources().size();
    auto &CE = Catalog::Get().get_database_in_use().cardinality_estimator();

    auto source_plans = std::make_unique<Producer*[]>(num_sources);
    for (auto &ds : G.sources()) {
        Subproblem s = Subproblem::Singleton(ds->id());
        if (auto bt = cast<BaseTable>(ds.get())) {
            /* Produce a scan for base tables. */
            PT[s].cost = 0;
            PT[s].model = CE.estimate_scan(G, s);
            auto &store = bt->table().store();
            auto source = std::make_unique<ScanOperator>(store, bt->name().assert_not_none());

            /* Set operator information. */
            auto source_info = std::make_unique<OperatorInformation>();
            source_info->subproblem = s;
            source_info->estimated_cardinality = CE.predict_cardinality(*PT[s].model);
            source->info(std::move(source_info));

            source_plans[ds->id()] = source.release();
        } else {
            /* Recursively solve nested queries. */
            auto &Q = as<Query>(*ds);
            const bool old = std::exchange(needs_projection_, Q.alias().has_value()); // aliased nested queries need projection
            auto [sub_plan, sub] = optimize(Q.query_graph());
            needs_projection_ = old;

            /* If an alias for the nested query is given, prefix every attribute with the alias. */
            if (Q.alias().has_value()) {
                M_insist(is<ProjectionOperator>(sub_plan), "only projection may rename attributes");
                Schema S;
                for (auto &e : sub_plan->schema())
                    S.add({ Q.alias(), e.id.name }, e.type, e.constraints);
                sub_plan->schema() = S;
            }

            /* Update the plan table with the `DataModel` and cost of the nested query and save the plan in the array of
             * source plans. */
            PT[s].cost = sub.cost;
            sub.model->assign_to(s); // adapt model s.t. it describes the result of the current subproblem
            PT[s].model = std::move(sub.model);
            source_plans[ds->id()] = sub_plan.release();
        }

        /* Apply filter, if any. */
        if (ds->filter().size()) {
            /* Optimize the filter by splitting into smaller filters and ordering them. */
            std::vector<cnf::CNF> filters = Optimizer::optimize_filter(ds->filter());
            Producer *filtered_ds = source_plans[ds->id()];

            /* Construct a plan as a sequence of filters. */
            for (auto &&filter : filters) {
                /* Update data model with filter. */
                auto new_model = CE.estimate_filter(G, *PT[s].model, filter);
                PT[s].model = std::move(new_model);

                if (filter.size() == 1 and filter[0].size() > 1) { // disjunctive filter
                    auto tmp = std::make_unique<DisjunctiveFilterOperator>(std::move(filter));
                    tmp->add_child(filtered_ds);
                    filtered_ds = tmp.release();
                } else {
                    auto tmp = std::make_unique<FilterOperator>(std::move(filter));
                    tmp->add_child(filtered_ds);
                    filtered_ds = tmp.release();
                }

                /* Set operator information. */
                auto source_info = std::make_unique<OperatorInformation>();
                source_info->subproblem = s;
                source_info->estimated_cardinality = CE.predict_cardinality(*PT[s].model); // includes filters, if any
                filtered_ds->info(std::move(source_info));
            }

            source_plans[ds->id()] = filtered_ds;
        }
    }
    return source_plans;
}

template<typename PlanTable>
void Optimizer::optimize_join_order(const QueryGraph &G, PlanTable &PT) const
{
    Catalog &C = Catalog::Get();
    auto &CE = C.get_database_in_use().cardinality_estimator();

#ifndef NDEBUG
    if (Options::Get().statistics) {
        std::size_t num_CSGs = 0, num_CCPs = 0;
        const Subproblem All = Subproblem::All(G.num_sources());
        auto inc_CSGs = [&num_CSGs](Subproblem) { ++num_CSGs; };
        auto inc_CCPs = [&num_CCPs](Subproblem, Subproblem) { ++num_CCPs; };
        G.adjacency_matrix().for_each_CSG_undirected(All, inc_CSGs);
        G.adjacency_matrix().for_each_CSG_pair_undirected(All, inc_CCPs);
        std::cout << num_CSGs << " CSGs, " << num_CCPs << " CCPs" << std::endl;
    }
#endif

    M_TIME_EXPR(plan_enumerator()(G, cost_function(), PT), "Plan enumeration", C.timer());

    if (Options::Get().statistics) {
        std::cout << "Est. total cost: " << PT.get_final().cost
                  << "\nEst. result set size: " << CE.predict_cardinality(*PT.get_final().model)
                  << "\nPlan cost: " << PT[PT.get_final().left].cost + PT[PT.get_final().right].cost
                  << std::endl;
    }
}

template<typename PlanTable>
std::unique_ptr<Producer> Optimizer::construct_join_order(const QueryGraph &G, const PlanTable &PT,
                                                          const std::unique_ptr<Producer*[]> &source_plans) const
{
    auto &CE = Catalog::Get().get_database_in_use().cardinality_estimator();

    std::vector<std::reference_wrapper<Join>> joins;
    for (auto &J : G.joins()) joins.emplace_back(*J);

    /* Use nested lambdas to implement recursive lambda using CPS. */
    const auto construct_recursive = [&](Subproblem s) -> Producer* {
        auto construct_plan_impl = [&](Subproblem s, auto &construct_plan_rec) -> Producer* {
            auto subproblems = PT[s].get_subproblems();
            if (subproblems.empty()) {
                M_insist(s.size() == 1);
                return source_plans[*s.begin()];
            } else {
                /* Compute plan for each sub problem.  Must happen *before* calculating the join predicate. */
                std::vector<Producer*> sub_plans;
                for (auto sub : subproblems)
                    sub_plans.push_back(construct_plan_rec(sub, construct_plan_rec));

                /* Calculate the join predicate. */
                cnf::CNF join_condition;
                for (auto it = joins.begin(); it != joins.end(); ) {
                    Subproblem join_sources;
                    /* Compute subproblem of sources to join. */
                    for (auto ds : it->get().sources())
                        join_sources(ds.get().id()) = true;

                    if (join_sources.is_subset(s)) { // possible join
                        join_condition = join_condition and it->get().condition();
                        it = joins.erase(it);
                    } else {
                        ++it;
                    }
                }

                /* Construct the join. */
                auto join = std::make_unique<JoinOperator>(join_condition);
                for (auto sub_plan : sub_plans)
                    join->add_child(sub_plan);
                auto join_info = std::make_unique<OperatorInformation>();
                join_info->subproblem = s;
                join_info->estimated_cardinality = CE.predict_cardinality(*PT[s].model);
                join->info(std::move(join_info));
                return join.release();
            }
        };
        return construct_plan_impl(s, construct_plan_impl);
    };

    return std::unique_ptr<Producer>(construct_recursive(Subproblem::All(G.sources().size())));
}

std::unique_ptr<Producer> Optimizer::optimize_plan(QueryGraph &G, std::unique_ptr<Producer> plan, PlanTableEntry &entry)
const
{
    auto &CE = Catalog::Get().get_database_in_use().cardinality_estimator();

    /* Perform grouping. */
    if (not G.group_by().empty()) {
        /* Compute `DataModel` after grouping. */
        auto new_model = CE.estimate_grouping(G, *entry.model, G.group_by()); // TODO provide aggregates
        entry.model = std::move(new_model);
        // TODO pick "best" algorithm
        auto group_by = std::make_unique<GroupingOperator>(G.group_by(), G.aggregates());
        group_by->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = CE.predict_cardinality(*entry.model);

        group_by->info(std::move(info));
        plan = std::move(group_by);
    } else if (not G.aggregates().empty()) {
        /* Compute `DataModel` after grouping. */
        auto new_model = CE.estimate_grouping(G, *entry.model, std::vector<GroupingOperator::group_type>());
        entry.model = std::move(new_model);
        auto agg = std::make_unique<AggregationOperator>(G.aggregates());
        agg->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = CE.predict_cardinality(*entry.model);

        agg->info(std::move(info));
        plan = std::move(agg);
    }

    auto additional_projections = Optimizer::compute_projections_required_for_order_by(G.projections(), G.order_by());
    const bool requires_post_projection = not additional_projections.empty();

    /* Perform projection. */
    if (not additional_projections.empty() or not G.projections().empty()) {
        /* Merge original projections with additional projections. */
        additional_projections.insert(additional_projections.end(), G.projections().begin(), G.projections().end());
        auto projection = std::make_unique<ProjectionOperator>(std::move(additional_projections));
        projection->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = projection->child(0)->info().estimated_cardinality;

        projection->info(std::move(info));
        plan = std::move(projection);
    }

    /* Perform ordering. */
    if (not G.order_by().empty()) {
        // TODO estimate data model
        auto order_by = std::make_unique<SortingOperator>(G.order_by());
        order_by->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = order_by->child(0)->info().estimated_cardinality;

        order_by->info(std::move(info));
        plan = std::move(order_by);
    }

    /* Limit. */
    if (G.limit().limit or G.limit().offset) {
        /* Compute `DataModel` after limit. */
        auto new_model = CE.estimate_limit(G, *entry.model, G.limit().limit, G.limit().offset);
        entry.model = std::move(new_model);
        // TODO estimate data model
        auto limit = std::make_unique<LimitOperator>(G.limit().limit, G.limit().offset);
        limit->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = CE.predict_cardinality(*entry.model);

        limit->info(std::move(info));
        plan = std::move(limit);
    }

    /* Perform post-ordering projection. */
    if (requires_post_projection or (not is<ProjectionOperator>(plan) and needs_projection_)) {
        // TODO estimate data model
        /* Change aliased projections in designators with the alias as name since original projection is
         * performed beforehand. */
        std::vector<projection_type> adapted_projections;
        for (auto [expr, alias] : G.projections()) {
            if (alias.has_value()) {
                Token name(expr.get().tok.pos, alias.assert_not_none(), TK_IDENTIFIER);
                auto d = std::make_unique<const Designator>(Token::CreateArtificial(), Token::CreateArtificial(),
                                                            std::move(name), expr.get().type(), &expr.get());
                adapted_projections.emplace_back(*d, ThreadSafePooledOptionalString{});
                created_exprs_.emplace_back(std::move(d));
            } else {
                adapted_projections.emplace_back(expr, ThreadSafePooledOptionalString{});
            }
        }
        auto projection = std::make_unique<ProjectionOperator>(std::move(adapted_projections));
        projection->add_child(plan.release());

        /* Set operator information. */
        auto info = std::make_unique<OperatorInformation>();
        info->subproblem = Subproblem::All(G.sources().size());
        info->estimated_cardinality = projection->child(0)->info().estimated_cardinality;

        projection->info(std::move(info));
        plan = std::move(projection);
    }
    return plan;
}

#define DEFINE(PLANTABLE) \
template \
std::pair<std::unique_ptr<Producer>, PLANTABLE> \
Optimizer::optimize_with_plantable(QueryGraph&) const; \
template \
std::unique_ptr<Producer*[]> \
Optimizer::optimize_source_plans(const QueryGraph&, PLANTABLE&) const; \
template \
void \
Optimizer::optimize_join_order(const QueryGraph&, PLANTABLE&) const; \
template \
std::unique_ptr<Producer> \
Optimizer::construct_join_order(const QueryGraph&, const PLANTABLE&, const std::unique_ptr<Producer*[]>&) const
DEFINE(PlanTableSmallOrDense);
DEFINE(PlanTableLargeAndSparse);
#undef DEFINE
