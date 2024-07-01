from query_utility import Relation, Join, JoinGraph


########################################################################################################################
# JOB Queries
########################################################################################################################
def create_q1a():
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind = 'production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'top 250 rank'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'", "(mc.note LIKE '%(co-production)%' OR mc.note LIKE '%(presents)%')"], projections = ['note'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = [], projections = ['title', 'production_year'])
	relations = [ct, it, mc, mi_idx, t]

	j0 = Join(ct, mc, ["id"], ["company_type_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, mi_idx, ["id"], ["movie_id"])
	j3 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j4 = Join(it, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q1b():
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind = 'production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'bottom 10 rank'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'"], projections = ['note'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2005', 't.production_year <= 2010'], projections = ['title', 'production_year'])
	relations = [ct, it, mc, mi_idx, t]

	j0 = Join(ct, mc, ["id"], ["company_type_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, mi_idx, ["id"], ["movie_id"])
	j3 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j4 = Join(it, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q1c():
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind = 'production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'top 250 rank'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'", "mc.note LIKE '%(co-production)%'"], projections = ['note'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >2010'], projections = ['title', 'production_year'])
	relations = [ct, it, mc, mi_idx, t]

	j0 = Join(ct, mc, ["id"], ["company_type_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, mi_idx, ["id"], ["movie_id"])
	j3 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j4 = Join(it, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q1d():
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind = 'production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'bottom 10 rank'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(as Metro-Goldwyn-Mayer Pictures)%'"], projections = ['note'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >2000'], projections = ['title', 'production_year'])
	relations = [ct, it, mc, mi_idx, t]

	j0 = Join(ct, mc, ["id"], ["company_type_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, mi_idx, ["id"], ["movie_id"])
	j3 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j4 = Join(it, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q2a():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[de]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [cn, k, mc, mk, t]

	j0 = Join(cn, mc, ["id"], ["company_id"])
	j1 = Join(mc, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q2b():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[nl]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [cn, k, mc, mk, t]

	j0 = Join(cn, mc, ["id"], ["company_id"])
	j1 = Join(mc, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q2c():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[sm]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [cn, k, mc, mk, t]

	j0 = Join(cn, mc, ["id"], ["company_id"])
	j1 = Join(mc, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q2d():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [cn, k, mc, mk, t]

	j0 = Join(cn, mc, ["id"], ["company_id"])
	j1 = Join(mc, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q3a():
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword LIKE '%sequel%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title'])
	relations = [k, mi, mk, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j3 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q3b():
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword LIKE '%sequel%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info', 'movie_id'], filters = ["(mi.info = 'Bulgaria')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2010'], projections = ['title'])
	relations = [k, mi, mk, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j3 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q3c():
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword LIKE '%sequel%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 1990'], projections = ['title'])
	relations = [k, mi, mk, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j3 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q4a():
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword LIKE '%sequel%'"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '5.0'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title'])
	relations = [it, k, mi_idx, mk, t]

	j0 = Join(t, mi_idx, ["id"], ["movie_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j3 = Join(k, mk, ["id"], ["keyword_id"])
	j4 = Join(it, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q4b():
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword LIKE '%sequel%'"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '9.0'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2010'], projections = ['title'])
	relations = [it, k, mi_idx, mk, t]

	j0 = Join(t, mi_idx, ["id"], ["movie_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j3 = Join(k, mk, ["id"], ["keyword_id"])
	j4 = Join(it, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q4c():
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword LIKE '%sequel%'"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '2.0'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 1990'], projections = ['title'])
	relations = [it, k, mi_idx, mk, t]

	j0 = Join(t, mi_idx, ["id"], ["movie_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j3 = Join(k, mk, ["id"], ["keyword_id"])
	j4 = Join(it, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q5a():
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind = 'production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'note'], filters = ["mc.note LIKE '%(theatrical)%'", "mc.note LIKE '%(France)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German')"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title'])
	relations = [ct, it, mc, mi, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j3 = Join(ct, mc, ["id"], ["company_type_id"])
	j4 = Join(it, mi, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q5b():
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind = 'production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'note'], filters = ["mc.note LIKE '%(VHS)%'", "mc.note LIKE '%(USA)%'", "mc.note LIKE '%(1994)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'USA' OR mi.info = 'America')"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2010'], projections = ['title'])
	relations = [ct, it, mc, mi, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j3 = Join(ct, mc, ["id"], ["company_type_id"])
	j4 = Join(it, mi, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q5c():
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind = 'production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(TV)%'", "mc.note LIKE '%(USA)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 1990'], projections = ['title'])
	relations = [ct, it, mc, mi, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j3 = Join(ct, mc, ["id"], ["company_type_id"])
	j4 = Join(it, mi, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q6a():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword = 'marvel-cinematic-universe'"], projections = ['keyword'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE '%Downey%Robert%'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2010'], projections = ['title'])
	relations = [ci, k, mk, n, t]

	j0 = Join(k, mk, ["id"], ["keyword_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j4 = Join(n, ci, ["id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q6b():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'superhero' OR k.keyword = 'sequel' OR k.keyword = 'second-part' OR k.keyword = 'marvel-comics' OR k.keyword = 'based-on-comic' OR k.keyword = 'tv-special' OR k.keyword = 'fight' OR k.keyword = 'violence')"], projections = ['keyword'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE '%Downey%Robert%'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2014'], projections = ['title'])
	relations = [ci, k, mk, n, t]

	j0 = Join(k, mk, ["id"], ["keyword_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j4 = Join(n, ci, ["id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q6c():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword = 'marvel-cinematic-universe'"], projections = ['keyword'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE '%Downey%Robert%'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2014'], projections = ['title'])
	relations = [ci, k, mk, n, t]

	j0 = Join(k, mk, ["id"], ["keyword_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j4 = Join(n, ci, ["id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q6d():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'superhero' OR k.keyword = 'sequel' OR k.keyword = 'second-part' OR k.keyword = 'marvel-comics' OR k.keyword = 'based-on-comic' OR k.keyword = 'tv-special' OR k.keyword = 'fight' OR k.keyword = 'violence')"], projections = ['keyword'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE '%Downey%Robert%'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [ci, k, mk, n, t]

	j0 = Join(k, mk, ["id"], ["keyword_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j4 = Join(n, ci, ["id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q6e():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword = 'marvel-cinematic-universe'"], projections = ['keyword'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE '%Downey%Robert%'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [ci, k, mk, n, t]

	j0 = Join(k, mk, ["id"], ["keyword_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j4 = Join(n, ci, ["id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q6f():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'superhero' OR k.keyword = 'sequel' OR k.keyword = 'second-part' OR k.keyword = 'marvel-comics' OR k.keyword = 'based-on-comic' OR k.keyword = 'tv-special' OR k.keyword = 'fight' OR k.keyword = 'violence')"], projections = ['keyword'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = [], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [ci, k, mk, n, t]

	j0 = Join(k, mk, ["id"], ["keyword_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j4 = Join(n, ci, ["id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q7a():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = ["an.name LIKE '%a%'"], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='mini biography'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link ='features'"], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['linked_movie_id', 'link_type_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'name', 'id', 'name_pcode_cf'], filters = ["n.name_pcode_cf >= 'A'", "n.name_pcode_cf <= 'F'", "(n.gender='m' OR (n.gender = 'f' AND n.name LIKE 'B%'))"], projections = ['name'])
	pi = Relation(name = "person_info", alias = "pi", attributes = ['person_id', 'info_type_id', 'note'], filters = ["pi.note ='Volker Boehm'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 1980', 't.production_year <= 1995'], projections = ['title'])
	relations = [an, ci, it, lt, ml, n, pi, t]

	j0 = Join(n, an, ["id"], ["person_id"])
	j1 = Join(n, pi, ["id"], ["person_id"])
	j2 = Join(ci, n, ["person_id"], ["id"])
	j3 = Join(t, ci, ["id"], ["movie_id"])
	j4 = Join(ml, t, ["linked_movie_id"], ["id"])
	j5 = Join(lt, ml, ["id"], ["link_type_id"])
	j6 = Join(it, pi, ["id"], ["info_type_id"])
	j7 = Join(pi, an, ["person_id"], ["person_id"])
	j8 = Join(pi, ci, ["person_id"], ["person_id"])
	j9 = Join(an, ci, ["person_id"], ["person_id"])
	j10 = Join(ci, ml, ["movie_id"], ["linked_movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q7b():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = ["an.name LIKE '%a%'"], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='mini biography'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link ='features'"], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['linked_movie_id', 'link_type_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'name', 'id', 'name_pcode_cf'], filters = ["n.name_pcode_cf LIKE 'D%'", "n.gender='m'"], projections = ['name'])
	pi = Relation(name = "person_info", alias = "pi", attributes = ['person_id', 'info_type_id', 'note'], filters = ["pi.note ='Volker Boehm'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 1980', 't.production_year <= 1984'], projections = ['title'])
	relations = [an, ci, it, lt, ml, n, pi, t]

	j0 = Join(n, an, ["id"], ["person_id"])
	j1 = Join(n, pi, ["id"], ["person_id"])
	j2 = Join(ci, n, ["person_id"], ["id"])
	j3 = Join(t, ci, ["id"], ["movie_id"])
	j4 = Join(ml, t, ["linked_movie_id"], ["id"])
	j5 = Join(lt, ml, ["id"], ["link_type_id"])
	j6 = Join(it, pi, ["id"], ["info_type_id"])
	j7 = Join(pi, an, ["person_id"], ["person_id"])
	j8 = Join(pi, ci, ["person_id"], ["person_id"])
	j9 = Join(an, ci, ["person_id"], ["person_id"])
	j10 = Join(ci, ml, ["movie_id"], ["linked_movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q7c():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = ["an.name IS NOT NULL", "(an.name LIKE '%a%' OR an.name LIKE 'A%')"], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='mini biography'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["(lt.link = 'references' OR lt.link = 'referenced in' OR lt.link = 'features' OR lt.link = 'featured in')"], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['linked_movie_id', 'link_type_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['gender', 'name', 'id', 'name_pcode_cf'], filters = ["n.name_pcode_cf >= 'A'", "n.name_pcode_cf <= 'F'", "(n.gender='m' OR (n.gender = 'f' AND n.name LIKE 'A%'))"], projections = ['name'])
	pi = Relation(name = "person_info", alias = "pi", attributes = ['person_id', 'info_type_id', 'note', 'info'], filters = ["pi.note IS NOT NULL"], projections = ['info'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 1980', 't.production_year <= 2010'], projections = [])
	relations = [an, ci, it, lt, ml, n, pi, t]

	j0 = Join(n, an, ["id"], ["person_id"])
	j1 = Join(n, pi, ["id"], ["person_id"])
	j2 = Join(ci, n, ["person_id"], ["id"])
	j3 = Join(t, ci, ["id"], ["movie_id"])
	j4 = Join(ml, t, ["linked_movie_id"], ["id"])
	j5 = Join(lt, ml, ["id"], ["link_type_id"])
	j6 = Join(it, pi, ["id"], ["info_type_id"])
	j7 = Join(pi, an, ["person_id"], ["person_id"])
	j8 = Join(pi, ci, ["person_id"], ["person_id"])
	j9 = Join(an, ci, ["person_id"], ["person_id"])
	j10 = Join(ci, ml, ["movie_id"], ["linked_movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q8a():
	an1 = Relation(name = "aka_name", alias = "an1", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'role_id', 'movie_id', 'note'], filters = ["ci.note ='(voice: English version)'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[jp]'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'movie_id', 'note'], filters = ["mc.note LIKE '%(Japan)%'", "mc.note NOT LIKE '%(USA)%'"], projections = [])
	n1 = Relation(name = "name", alias = "n1", attributes = ['name', 'id'], filters = ["n1.name LIKE '%Yo%'", "n1.name NOT LIKE '%Yu%'"], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [an1, ci, cn, mc, n1, rt, t]

	j0 = Join(an1, n1, ["person_id"], ["id"])
	j1 = Join(n1, ci, ["id"], ["person_id"])
	j2 = Join(ci, t, ["movie_id"], ["id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(mc, cn, ["company_id"], ["id"])
	j5 = Join(ci, rt, ["role_id"], ["id"])
	j6 = Join(an1, ci, ["person_id"], ["person_id"])
	j7 = Join(ci, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q8b():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'role_id', 'movie_id', 'note'], filters = ["ci.note ='(voice: English version)'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[jp]'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'movie_id', 'note'], filters = ["mc.note LIKE '%(Japan)%'", "mc.note NOT LIKE '%(USA)%'", "(mc.note LIKE '%(2006)%' OR mc.note LIKE '%(2007)%')"], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE '%Yo%'", "n.name NOT LIKE '%Yu%'"], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2006', 't.production_year <= 2007', "(t.title LIKE 'One Piece%' OR t.title LIKE 'Dragon Ball Z%')"], projections = ['title'])
	relations = [an, ci, cn, mc, n, rt, t]

	j0 = Join(an, n, ["person_id"], ["id"])
	j1 = Join(n, ci, ["id"], ["person_id"])
	j2 = Join(ci, t, ["movie_id"], ["id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(mc, cn, ["company_id"], ["id"])
	j5 = Join(ci, rt, ["role_id"], ["id"])
	j6 = Join(an, ci, ["person_id"], ["person_id"])
	j7 = Join(ci, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q8c():
	a1 = Relation(name = "aka_name", alias = "a1", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'role_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	n1 = Relation(name = "name", alias = "n1", attributes = ['id'], filters = [], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='writer'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [a1, ci, cn, mc, n1, rt, t]

	j0 = Join(a1, n1, ["person_id"], ["id"])
	j1 = Join(n1, ci, ["id"], ["person_id"])
	j2 = Join(ci, t, ["movie_id"], ["id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(mc, cn, ["company_id"], ["id"])
	j5 = Join(ci, rt, ["role_id"], ["id"])
	j6 = Join(a1, ci, ["person_id"], ["person_id"])
	j7 = Join(ci, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q8d():
	an1 = Relation(name = "aka_name", alias = "an1", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'role_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	n1 = Relation(name = "name", alias = "n1", attributes = ['id'], filters = [], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='costume designer'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [an1, ci, cn, mc, n1, rt, t]

	j0 = Join(an1, n1, ["person_id"], ["id"])
	j1 = Join(n1, ci, ["id"], ["person_id"])
	j2 = Join(ci, t, ["movie_id"], ["id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(mc, cn, ["company_id"], ["id"])
	j5 = Join(ci, rt, ["role_id"], ["id"])
	j6 = Join(an1, ci, ["person_id"], ["person_id"])
	j7 = Join(ci, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7]

	return JoinGraph(relations, joins)

def create_q9a():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'movie_id', 'note'], filters = ['mc.note IS NOT NULL', "(mc.note LIKE '%(USA)%' OR mc.note LIKE '%(worldwide)%')"], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%Ang%'"], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2005', 't.production_year <= 2015'], projections = ['title'])
	relations = [an, chn, ci, cn, mc, n, rt, t]

	j0 = Join(ci, t, ["movie_id"], ["id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j3 = Join(mc, cn, ["company_id"], ["id"])
	j4 = Join(ci, rt, ["role_id"], ["id"])
	j5 = Join(n, ci, ["id"], ["person_id"])
	j6 = Join(chn, ci, ["id"], ["person_role_id"])
	j7 = Join(an, n, ["person_id"], ["id"])
	j8 = Join(an, ci, ["person_id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q9b():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["ci.note = '(voice)'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'movie_id', 'note'], filters = ["mc.note LIKE '%(200%)%'", "(mc.note LIKE '%(USA)%' OR mc.note LIKE '%(worldwide)%')"], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%Angel%'"], projections = ['name'])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2007', 't.production_year <= 2010'], projections = ['title'])
	relations = [an, chn, ci, cn, mc, n, rt, t]

	j0 = Join(ci, t, ["movie_id"], ["id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j3 = Join(mc, cn, ["company_id"], ["id"])
	j4 = Join(ci, rt, ["role_id"], ["id"])
	j5 = Join(n, ci, ["id"], ["person_id"])
	j6 = Join(chn, ci, ["id"], ["person_role_id"])
	j7 = Join(an, n, ["person_id"], ["id"])
	j8 = Join(an, ci, ["person_id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q9c():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%An%'"], projections = ['name'])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [an, chn, ci, cn, mc, n, rt, t]

	j0 = Join(ci, t, ["movie_id"], ["id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j3 = Join(mc, cn, ["company_id"], ["id"])
	j4 = Join(ci, rt, ["role_id"], ["id"])
	j5 = Join(n, ci, ["id"], ["person_id"])
	j6 = Join(chn, ci, ["id"], ["person_role_id"])
	j7 = Join(an, n, ["person_id"], ["id"])
	j8 = Join(an, ci, ["person_id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q9d():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'"], projections = ['name'])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [an, chn, ci, cn, mc, n, rt, t]

	j0 = Join(ci, t, ["movie_id"], ["id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j3 = Join(mc, cn, ["company_id"], ["id"])
	j4 = Join(ci, rt, ["role_id"], ["id"])
	j5 = Join(n, ci, ["id"], ["person_id"])
	j6 = Join(chn, ci, ["id"], ["person_role_id"])
	j7 = Join(an, n, ["person_id"], ["id"])
	j8 = Join(an, ci, ["person_id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q10a():
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_role_id', 'role_id', 'movie_id', 'note'], filters = ["ci.note LIKE '%(voice)%'", "ci.note LIKE '%(uncredited)%'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code = '[ru]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role = 'actor'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title'])
	relations = [chn, ci, cn, ct, mc, rt, t]

	j0 = Join(t, mc, ["id"], ["movie_id"])
	j1 = Join(t, ci, ["id"], ["movie_id"])
	j2 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j3 = Join(chn, ci, ["id"], ["person_role_id"])
	j4 = Join(rt, ci, ["id"], ["role_id"])
	j5 = Join(cn, mc, ["id"], ["company_id"])
	j6 = Join(ct, mc, ["id"], ["company_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q10b():
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_role_id', 'role_id', 'movie_id', 'note'], filters = ["ci.note LIKE '%(producer)%'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code = '[ru]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role = 'actor'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2010'], projections = ['title'])
	relations = [chn, ci, cn, ct, mc, rt, t]

	j0 = Join(t, mc, ["id"], ["movie_id"])
	j1 = Join(t, ci, ["id"], ["movie_id"])
	j2 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j3 = Join(chn, ci, ["id"], ["person_role_id"])
	j4 = Join(rt, ci, ["id"], ["role_id"])
	j5 = Join(cn, mc, ["id"], ["company_id"])
	j6 = Join(ct, mc, ["id"], ["company_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q10c():
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_role_id', 'role_id', 'movie_id', 'note'], filters = ["ci.note LIKE '%(producer)%'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code = '[us]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 1990'], projections = ['title'])
	relations = [chn, ci, cn, ct, mc, rt, t]

	j0 = Join(t, mc, ["id"], ["movie_id"])
	j1 = Join(t, ci, ["id"], ["movie_id"])
	j2 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j3 = Join(chn, ci, ["id"], ["person_role_id"])
	j4 = Join(rt, ci, ["id"], ["role_id"])
	j5 = Join(cn, mc, ["id"], ["company_id"])
	j6 = Join(ct, mc, ["id"], ["company_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6]

	return JoinGraph(relations, joins)

def create_q11a():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'", "(cn.name LIKE '%Film%' OR cn.name LIKE '%Warner%')"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='sequel'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link LIKE '%follow%'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NULL'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year >= 1950', 't.production_year <= 2000'], projections = [])
	relations = [cn, ct, k, lt, mc, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mk, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q11b():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'", "(cn.name LIKE '%Film%' OR cn.name LIKE '%Warner%')"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='sequel'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link LIKE '%follows%'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NULL'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year = 1998', "t.title LIKE '%Money%'"], projections = [])
	relations = [cn, ct, k, lt, mc, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mk, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q11c():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'", "(cn.name LIKE '20th Century Fox%' OR cn.name LIKE 'Twentieth Century Fox%')"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind != 'production companies'", 'ct.kind IS NOT NULL'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'sequel' OR k.keyword = 'revenge' OR k.keyword = 'based-on-novel')"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NOT NULL'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year > 1950'], projections = [])
	relations = [cn, ct, k, lt, mc, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mk, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q11d():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind != 'production companies'", 'ct.kind IS NOT NULL'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'sequel' OR k.keyword = 'revenge' OR k.keyword = 'based-on-novel')"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NOT NULL'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year > 1950'], projections = [])
	relations = [cn, ct, k, lt, mc, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mk, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q12a():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code = '[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind = 'production companies'"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Drama' OR mi.info = 'Horror')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '8.0'"], projections = ['info'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2005', 't.production_year <= 2008'], projections = ['title'])
	relations = [cn, ct, it1, it2, mc, mi, mi_idx, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(mi, it1, ["info_type_id"], ["id"])
	j3 = Join(mi_idx, it2, ["info_type_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(ct, mc, ["id"], ["company_type_id"])
	j6 = Join(cn, mc, ["id"], ["company_id"])
	j7 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j8 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q12b():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ['ct.kind IS NOT NULL', "(ct.kind ='production companies' OR ct.kind = 'distributors')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info ='budget'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info ='bottom 10 rank'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >2000', "(t.title LIKE 'Birdemic%' OR t.title LIKE '%Movie%')"], projections = ['title'])
	relations = [cn, ct, it1, it2, mc, mi, mi_idx, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(mi, it1, ["info_type_id"], ["id"])
	j3 = Join(mi_idx, it2, ["info_type_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(ct, mc, ["id"], ["company_type_id"])
	j6 = Join(cn, mc, ["id"], ["company_id"])
	j7 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j8 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q12c():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code = '[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind = 'production companies'"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Drama' OR mi.info = 'Horror' OR mi.info = 'Western' OR mi.info = 'Family')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '7.0'"], projections = ['info'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2000', 't.production_year <= 2010'], projections = ['title'])
	relations = [cn, ct, it1, it2, mc, mi, mi_idx, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(mi, it1, ["info_type_id"], ["id"])
	j3 = Join(mi_idx, it2, ["info_type_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(ct, mc, ["id"], ["company_type_id"])
	j6 = Join(cn, mc, ["id"], ["company_id"])
	j7 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j8 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q13a():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[de]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='rating'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info ='release dates'"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind ='movie'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	miidx = Relation(name = "movie_info_idx", alias = "miidx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	t = Relation(name = "title", alias = "t", attributes = ['kind_id', 'id', 'title'], filters = [], projections = ['title'])
	relations = [cn, ct, it, it2, kt, mc, mi, miidx, t]

	j0 = Join(mi, t, ["movie_id"], ["id"])
	j1 = Join(it2, mi, ["id"], ["info_type_id"])
	j2 = Join(kt, t, ["id"], ["kind_id"])
	j3 = Join(mc, t, ["movie_id"], ["id"])
	j4 = Join(cn, mc, ["id"], ["company_id"])
	j5 = Join(ct, mc, ["id"], ["company_type_id"])
	j6 = Join(miidx, t, ["movie_id"], ["id"])
	j7 = Join(it, miidx, ["id"], ["info_type_id"])
	j8 = Join(mi, miidx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j10 = Join(miidx, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q13b():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code ='[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='rating'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info ='release dates'"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind ='movie'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id'], filters = [], projections = [])
	miidx = Relation(name = "movie_info_idx", alias = "miidx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	t = Relation(name = "title", alias = "t", attributes = ['kind_id', 'id', 'title'], filters = ["t.title != ''", "(t.title LIKE '%Champion%' OR t.title LIKE '%Loser%')"], projections = ['title'])
	relations = [cn, ct, it, it2, kt, mc, mi, miidx, t]

	j0 = Join(mi, t, ["movie_id"], ["id"])
	j1 = Join(it2, mi, ["id"], ["info_type_id"])
	j2 = Join(kt, t, ["id"], ["kind_id"])
	j3 = Join(mc, t, ["movie_id"], ["id"])
	j4 = Join(cn, mc, ["id"], ["company_id"])
	j5 = Join(ct, mc, ["id"], ["company_type_id"])
	j6 = Join(miidx, t, ["movie_id"], ["id"])
	j7 = Join(it, miidx, ["id"], ["info_type_id"])
	j8 = Join(mi, miidx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j10 = Join(miidx, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q13c():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code ='[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='rating'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info ='release dates'"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind ='movie'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id'], filters = [], projections = [])
	miidx = Relation(name = "movie_info_idx", alias = "miidx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	t = Relation(name = "title", alias = "t", attributes = ['kind_id', 'id', 'title'], filters = ["t.title != ''", "(t.title LIKE 'Champion%' OR t.title LIKE 'Loser%')"], projections = ['title'])
	relations = [cn, ct, it, it2, kt, mc, mi, miidx, t]

	j0 = Join(mi, t, ["movie_id"], ["id"])
	j1 = Join(it2, mi, ["id"], ["info_type_id"])
	j2 = Join(kt, t, ["id"], ["kind_id"])
	j3 = Join(mc, t, ["movie_id"], ["id"])
	j4 = Join(cn, mc, ["id"], ["company_id"])
	j5 = Join(ct, mc, ["id"], ["company_type_id"])
	j6 = Join(miidx, t, ["movie_id"], ["id"])
	j7 = Join(it, miidx, ["id"], ["info_type_id"])
	j8 = Join(mi, miidx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j10 = Join(miidx, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q13d():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code ='[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='rating'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info ='release dates'"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind ='movie'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id'], filters = [], projections = [])
	miidx = Relation(name = "movie_info_idx", alias = "miidx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	t = Relation(name = "title", alias = "t", attributes = ['kind_id', 'id', 'title'], filters = [], projections = ['title'])
	relations = [cn, ct, it, it2, kt, mc, mi, miidx, t]

	j0 = Join(mi, t, ["movie_id"], ["id"])
	j1 = Join(it2, mi, ["id"], ["info_type_id"])
	j2 = Join(kt, t, ["id"], ["kind_id"])
	j3 = Join(mc, t, ["movie_id"], ["id"])
	j4 = Join(cn, mc, ["id"], ["company_id"])
	j5 = Join(ct, mc, ["id"], ["company_type_id"])
	j6 = Join(miidx, t, ["movie_id"], ["id"])
	j7 = Join(it, miidx, ["id"], ["info_type_id"])
	j8 = Join(mi, miidx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j10 = Join(miidx, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q14a():
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind = 'movie'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info < '8.5'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2010'], projections = ['title'])
	relations = [it1, it2, k, kt, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(k, mk, ["id"], ["keyword_id"])
	j8 = Join(it1, mi, ["id"], ["info_type_id"])
	j9 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q14b():
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind = 'movie'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '6.0'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2010', "(t.title LIKE '%murder%' OR t.title LIKE '%Murder%' OR t.title LIKE '%Mord%')"], projections = ['title'])
	relations = [it1, it2, k, kt, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(k, mk, ["id"], ["keyword_id"])
	j8 = Join(it1, mi, ["id"], ["info_type_id"])
	j9 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q14c():
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ['k.keyword IS NOT NULL', "(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'episode')"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Danish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info < '8.5'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title'])
	relations = [it1, it2, k, kt, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(k, mk, ["id"], ["keyword_id"])
	j8 = Join(it1, mi, ["id"], ["info_type_id"])
	j9 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q15a():
	at = Relation(name = "aka_title", alias = "at", attributes = ['movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code = '[us]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'release dates'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ["mc.note LIKE '%(200%)%'", "mc.note LIKE '%(worldwide)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id', 'info', 'note'], filters = ["mi.note LIKE '%internet%'", "mi.info LIKE 'USA:% 200%'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [at, cn, ct, it1, k, mc, mi, mk, t]

	j0 = Join(t, at, ["id"], ["movie_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j6 = Join(mk, at, ["movie_id"], ["movie_id"])
	j7 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, at, ["movie_id"], ["movie_id"])
	j9 = Join(mc, at, ["movie_id"], ["movie_id"])
	j10 = Join(k, mk, ["id"], ["keyword_id"])
	j11 = Join(it1, mi, ["id"], ["info_type_id"])
	j12 = Join(cn, mc, ["id"], ["company_id"])
	j13 = Join(ct, mc, ["id"], ["company_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q15b():
	at = Relation(name = "aka_title", alias = "at", attributes = ['movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'country_code', 'id'], filters = ["cn.country_code = '[us]'", "cn.name = 'YouTube'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'release dates'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ["mc.note LIKE '%(200%)%'", "mc.note LIKE '%(worldwide)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id', 'info', 'note'], filters = ["mi.note LIKE '%internet%'", "mi.info LIKE 'USA:% 200%'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2005', 't.production_year <= 2010'], projections = ['title'])
	relations = [at, cn, ct, it1, k, mc, mi, mk, t]

	j0 = Join(t, at, ["id"], ["movie_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j6 = Join(mk, at, ["movie_id"], ["movie_id"])
	j7 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, at, ["movie_id"], ["movie_id"])
	j9 = Join(mc, at, ["movie_id"], ["movie_id"])
	j10 = Join(k, mk, ["id"], ["keyword_id"])
	j11 = Join(it1, mi, ["id"], ["info_type_id"])
	j12 = Join(cn, mc, ["id"], ["company_id"])
	j13 = Join(ct, mc, ["id"], ["company_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q15c():
	at = Relation(name = "aka_title", alias = "at", attributes = ['movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code = '[us]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'release dates'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id', 'info', 'note'], filters = ["mi.note LIKE '%internet%'", 'mi.info IS NOT NULL', "(mi.info LIKE 'USA:% 199%' OR mi.info LIKE 'USA:% 200%')"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 1990'], projections = ['title'])
	relations = [at, cn, ct, it1, k, mc, mi, mk, t]

	j0 = Join(t, at, ["id"], ["movie_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j6 = Join(mk, at, ["movie_id"], ["movie_id"])
	j7 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, at, ["movie_id"], ["movie_id"])
	j9 = Join(mc, at, ["movie_id"], ["movie_id"])
	j10 = Join(k, mk, ["id"], ["keyword_id"])
	j11 = Join(it1, mi, ["id"], ["info_type_id"])
	j12 = Join(cn, mc, ["id"], ["company_id"])
	j13 = Join(ct, mc, ["id"], ["company_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q15d():
	at = Relation(name = "aka_title", alias = "at", attributes = ['title', 'movie_id'], filters = [], projections = ['title'])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code = '[us]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'release dates'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id', 'note'], filters = ["mi.note LIKE '%internet%'"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 1990'], projections = ['title'])
	relations = [at, cn, ct, it1, k, mc, mi, mk, t]

	j0 = Join(t, at, ["id"], ["movie_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j6 = Join(mk, at, ["movie_id"], ["movie_id"])
	j7 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, at, ["movie_id"], ["movie_id"])
	j9 = Join(mc, at, ["movie_id"], ["movie_id"])
	j10 = Join(k, mk, ["id"], ["keyword_id"])
	j11 = Join(it1, mi, ["id"], ["info_type_id"])
	j12 = Join(cn, mc, ["id"], ["company_id"])
	j13 = Join(ct, mc, ["id"], ["company_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q16a():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'episode_nr', 'title'], filters = ['t.episode_nr >= 50', 't.episode_nr < 100'], projections = ['title'])
	relations = [an, ci, cn, k, mc, mk, n, t]

	j0 = Join(an, n, ["person_id"], ["id"])
	j1 = Join(n, ci, ["id"], ["person_id"])
	j2 = Join(ci, t, ["movie_id"], ["id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(mk, k, ["keyword_id"], ["id"])
	j5 = Join(t, mc, ["id"], ["movie_id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(an, ci, ["person_id"], ["person_id"])
	j8 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j9 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j10 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q16b():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [an, ci, cn, k, mc, mk, n, t]

	j0 = Join(an, n, ["person_id"], ["id"])
	j1 = Join(n, ci, ["id"], ["person_id"])
	j2 = Join(ci, t, ["movie_id"], ["id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(mk, k, ["keyword_id"], ["id"])
	j5 = Join(t, mc, ["id"], ["movie_id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(an, ci, ["person_id"], ["person_id"])
	j8 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j9 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j10 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q16c():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'episode_nr', 'title'], filters = ['t.episode_nr < 100'], projections = ['title'])
	relations = [an, ci, cn, k, mc, mk, n, t]

	j0 = Join(an, n, ["person_id"], ["id"])
	j1 = Join(n, ci, ["id"], ["person_id"])
	j2 = Join(ci, t, ["movie_id"], ["id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(mk, k, ["keyword_id"], ["id"])
	j5 = Join(t, mc, ["id"], ["movie_id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(an, ci, ["person_id"], ["person_id"])
	j8 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j9 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j10 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q16d():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'episode_nr', 'title'], filters = ['t.episode_nr >= 5', 't.episode_nr < 100'], projections = ['title'])
	relations = [an, ci, cn, k, mc, mk, n, t]

	j0 = Join(an, n, ["person_id"], ["id"])
	j1 = Join(n, ci, ["id"], ["person_id"])
	j2 = Join(ci, t, ["movie_id"], ["id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(mk, k, ["keyword_id"], ["id"])
	j5 = Join(t, mc, ["id"], ["movie_id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(an, ci, ["person_id"], ["person_id"])
	j8 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j9 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j10 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q17a():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE 'B%'"], projections = ['name', 'name'])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [ci, cn, k, mc, mk, n, t]

	j0 = Join(n, ci, ["id"], ["person_id"])
	j1 = Join(ci, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, cn, ["company_id"], ["id"])
	j6 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q17b():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE 'Z%'"], projections = ['name', 'name'])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [ci, cn, k, mc, mk, n, t]

	j0 = Join(n, ci, ["id"], ["person_id"])
	j1 = Join(ci, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, cn, ["company_id"], ["id"])
	j6 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q17c():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE 'X%'"], projections = ['name', 'name'])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [ci, cn, k, mc, mk, n, t]

	j0 = Join(n, ci, ["id"], ["person_id"])
	j1 = Join(ci, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, cn, ["company_id"], ["id"])
	j6 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q17d():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE '%Bert%'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [ci, cn, k, mc, mk, n, t]

	j0 = Join(n, ci, ["id"], ["person_id"])
	j1 = Join(ci, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, cn, ["company_id"], ["id"])
	j6 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q17e():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = [], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [ci, cn, k, mc, mk, n, t]

	j0 = Join(n, ci, ["id"], ["person_id"])
	j1 = Join(ci, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, cn, ["company_id"], ["id"])
	j6 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q17f():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE '%B%'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['id'], filters = [], projections = [])
	relations = [ci, cn, k, mc, mk, n, t]

	j0 = Join(n, ci, ["id"], ["person_id"])
	j1 = Join(ci, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, cn, ["company_id"], ["id"])
	j6 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q18a():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(producer)' OR ci.note = '(executive producer)')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'budget'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender = 'm'", "n.name LIKE '%Tim%'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [ci, it1, it2, mi, mi_idx, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j4 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j5 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(n, ci, ["id"], ["person_id"])
	j7 = Join(it1, mi, ["id"], ["info_type_id"])
	j8 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q18b():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id', 'info', 'note'], filters = ["(mi.info = 'Horror' OR mi.info = 'Thriller')", 'mi.note IS NULL'], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '8.0'"], projections = ['info'])
	n = Relation(name = "name", alias = "n", attributes = ['id', 'gender'], filters = ['n.gender IS NOT NULL', "n.gender = 'f'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2008', 't.production_year <= 2014'], projections = ['title'])
	relations = [ci, it1, it2, mi, mi_idx, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j4 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j5 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(n, ci, ["id"], ["person_id"])
	j7 = Join(it1, mi, ["id"], ["info_type_id"])
	j8 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q18c():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Horror' OR mi.info = 'Action' OR mi.info = 'Sci-Fi' OR mi.info = 'Thriller' OR mi.info = 'Crime' OR mi.info = 'War')"], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	n = Relation(name = "name", alias = "n", attributes = ['id', 'gender'], filters = ["n.gender = 'm'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [ci, it1, it2, mi, mi_idx, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j4 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j5 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(n, ci, ["id"], ["person_id"])
	j7 = Join(it1, mi, ["id"], ["info_type_id"])
	j8 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q19a():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['id'], filters = [], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'release dates'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'movie_id', 'note'], filters = ['mc.note IS NOT NULL', "(mc.note LIKE '%(USA)%' OR mc.note LIKE '%(worldwide)%')"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ['mi.info IS NOT NULL', "(mi.info LIKE 'Japan:%200%' OR mi.info LIKE 'USA:%200%')"], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%Ang%'"], projections = ['name'])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2005', 't.production_year <= 2009'], projections = ['title'])
	relations = [an, chn, ci, cn, it, mc, mi, n, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(mc, ci, ["movie_id"], ["movie_id"])
	j4 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mi, ci, ["movie_id"], ["movie_id"])
	j6 = Join(cn, mc, ["id"], ["company_id"])
	j7 = Join(it, mi, ["id"], ["info_type_id"])
	j8 = Join(n, ci, ["id"], ["person_id"])
	j9 = Join(rt, ci, ["id"], ["role_id"])
	j10 = Join(n, an, ["id"], ["person_id"])
	j11 = Join(ci, an, ["person_id"], ["person_id"])
	j12 = Join(chn, ci, ["id"], ["person_role_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12]

	return JoinGraph(relations, joins)

def create_q19b():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['id'], filters = [], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["ci.note = '(voice)'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'release dates'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'movie_id', 'note'], filters = ["mc.note LIKE '%(200%)%'", "(mc.note LIKE '%(USA)%' OR mc.note LIKE '%(worldwide)%')"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ['mi.info IS NOT NULL', "(mi.info LIKE 'Japan:%2007%' OR mi.info LIKE 'USA:%2008%')"], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%Angel%'"], projections = ['name'])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2007', 't.production_year <= 2008', "t.title LIKE '%Kung%Fu%Panda%'"], projections = ['title'])
	relations = [an, chn, ci, cn, it, mc, mi, n, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(mc, ci, ["movie_id"], ["movie_id"])
	j4 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mi, ci, ["movie_id"], ["movie_id"])
	j6 = Join(cn, mc, ["id"], ["company_id"])
	j7 = Join(it, mi, ["id"], ["info_type_id"])
	j8 = Join(n, ci, ["id"], ["person_id"])
	j9 = Join(rt, ci, ["id"], ["role_id"])
	j10 = Join(n, an, ["id"], ["person_id"])
	j11 = Join(ci, an, ["person_id"], ["person_id"])
	j12 = Join(chn, ci, ["id"], ["person_role_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12]

	return JoinGraph(relations, joins)

def create_q19c():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['id'], filters = [], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'release dates'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ['mi.info IS NOT NULL', "(mi.info LIKE 'Japan:%200%' OR mi.info LIKE 'USA:%200%')"], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%An%'"], projections = ['name'])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [an, chn, ci, cn, it, mc, mi, n, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(mc, ci, ["movie_id"], ["movie_id"])
	j4 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mi, ci, ["movie_id"], ["movie_id"])
	j6 = Join(cn, mc, ["id"], ["company_id"])
	j7 = Join(it, mi, ["id"], ["info_type_id"])
	j8 = Join(n, ci, ["id"], ["person_id"])
	j9 = Join(rt, ci, ["id"], ["role_id"])
	j10 = Join(n, an, ["id"], ["person_id"])
	j11 = Join(ci, an, ["person_id"], ["person_id"])
	j12 = Join(chn, ci, ["id"], ["person_role_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12]

	return JoinGraph(relations, joins)

def create_q19d():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['id'], filters = [], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'release dates'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'"], projections = ['name'])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [an, chn, ci, cn, it, mc, mi, n, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(mc, ci, ["movie_id"], ["movie_id"])
	j4 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j5 = Join(mi, ci, ["movie_id"], ["movie_id"])
	j6 = Join(cn, mc, ["id"], ["company_id"])
	j7 = Join(it, mi, ["id"], ["info_type_id"])
	j8 = Join(n, ci, ["id"], ["person_id"])
	j9 = Join(rt, ci, ["id"], ["role_id"])
	j10 = Join(n, an, ["id"], ["person_id"])
	j11 = Join(ci, an, ["person_id"], ["person_id"])
	j12 = Join(chn, ci, ["id"], ["person_role_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12]

	return JoinGraph(relations, joins)

def create_q20a():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind LIKE '%complete%'"], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = ["chn.name NOT LIKE '%Sherlock%'", "(chn.name LIKE '%Tony%Stark%' OR chn.name LIKE '%Iron%Man%')"], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'person_role_id', 'movie_id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'superhero' OR k.keyword = 'sequel' OR k.keyword = 'second-part' OR k.keyword = 'marvel-comics' OR k.keyword = 'based-on-comic' OR k.keyword = 'tv-special' OR k.keyword = 'fight' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind = 'movie'"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 1950'], projections = ['title'])
	relations = [cc, cct1, cct2, chn, ci, k, kt, mk, n, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, cc, ["id"], ["movie_id"])
	j4 = Join(mk, ci, ["movie_id"], ["movie_id"])
	j5 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j6 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j7 = Join(chn, ci, ["id"], ["person_role_id"])
	j8 = Join(n, ci, ["id"], ["person_id"])
	j9 = Join(k, mk, ["id"], ["keyword_id"])
	j10 = Join(cct1, cc, ["id"], ["subject_id"])
	j11 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11]

	return JoinGraph(relations, joins)

def create_q20b():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind LIKE '%complete%'"], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = ["chn.name NOT LIKE '%Sherlock%'", "(chn.name LIKE '%Tony%Stark%' OR chn.name LIKE '%Iron%Man%')"], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'person_role_id', 'movie_id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'superhero' OR k.keyword = 'sequel' OR k.keyword = 'second-part' OR k.keyword = 'marvel-comics' OR k.keyword = 'based-on-comic' OR k.keyword = 'tv-special' OR k.keyword = 'fight' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind = 'movie'"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = ["n.name LIKE '%Downey%Robert%'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [cc, cct1, cct2, chn, ci, k, kt, mk, n, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, cc, ["id"], ["movie_id"])
	j4 = Join(mk, ci, ["movie_id"], ["movie_id"])
	j5 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j6 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j7 = Join(chn, ci, ["id"], ["person_role_id"])
	j8 = Join(n, ci, ["id"], ["person_id"])
	j9 = Join(k, mk, ["id"], ["keyword_id"])
	j10 = Join(cct1, cc, ["id"], ["subject_id"])
	j11 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11]

	return JoinGraph(relations, joins)

def create_q20c():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind LIKE '%complete%'"], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = ['chn.name IS NOT NULL', "(chn.name LIKE '%man%' OR chn.name LIKE '%Man%')"], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'person_role_id', 'movie_id'], filters = [], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'superhero' OR k.keyword = 'marvel-comics' OR k.keyword = 'based-on-comic' OR k.keyword = 'tv-special' OR k.keyword = 'fight' OR k.keyword = 'violence' OR k.keyword = 'magnet' OR k.keyword = 'web' OR k.keyword = 'claw' OR k.keyword = 'laser')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind = 'movie'"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = [], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [cc, cct1, cct2, chn, ci, k, kt, mk, n, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, cc, ["id"], ["movie_id"])
	j4 = Join(mk, ci, ["movie_id"], ["movie_id"])
	j5 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j6 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j7 = Join(chn, ci, ["id"], ["person_role_id"])
	j8 = Join(n, ci, ["id"], ["person_id"])
	j9 = Join(k, mk, ["id"], ["keyword_id"])
	j10 = Join(cct1, cc, ["id"], ["subject_id"])
	j11 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11]

	return JoinGraph(relations, joins)

def create_q21a():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'", "(cn.name LIKE '%Film%' OR cn.name LIKE '%Warner%')"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='sequel'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link LIKE '%follow%'"], projections = ['link'])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NULL'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 1950', 't.production_year <= 2000'], projections = ['title'])
	relations = [cn, ct, k, lt, mc, mi, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(mi, t, ["movie_id"], ["id"])
	j8 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j9 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j10 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j11 = Join(ml, mi, ["movie_id"], ["movie_id"])
	j12 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j13 = Join(mc, mi, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q21b():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'", "(cn.name LIKE '%Film%' OR cn.name LIKE '%Warner%')"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='sequel'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link LIKE '%follow%'"], projections = ['link'])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NULL'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info', 'movie_id'], filters = ["(mi.info = 'Germany' OR mi.info = 'German')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2000', 't.production_year <= 2010'], projections = ['title'])
	relations = [cn, ct, k, lt, mc, mi, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(mi, t, ["movie_id"], ["id"])
	j8 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j9 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j10 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j11 = Join(ml, mi, ["movie_id"], ["movie_id"])
	j12 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j13 = Join(mc, mi, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q21c():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'", "(cn.name LIKE '%Film%' OR cn.name LIKE '%Warner%')"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='sequel'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link LIKE '%follow%'"], projections = ['link'])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NULL'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'English')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 1950', 't.production_year <= 2010'], projections = ['title'])
	relations = [cn, ct, k, lt, mc, mi, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(mi, t, ["movie_id"], ["id"])
	j8 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j9 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j10 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j11 = Join(ml, mi, ["movie_id"], ["movie_id"])
	j12 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j13 = Join(mc, mi, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q22a():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code != '[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'episode')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(USA)%'", "mc.note LIKE '%(200%)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Germany' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info < '7.0'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2008'], projections = ['title'])
	relations = [cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j6 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j10 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(k, mk, ["id"], ["keyword_id"])
	j12 = Join(it1, mi, ["id"], ["info_type_id"])
	j13 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j14 = Join(ct, mc, ["id"], ["company_type_id"])
	j15 = Join(cn, mc, ["id"], ["company_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15]

	return JoinGraph(relations, joins)

def create_q22b():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code != '[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'episode')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(USA)%'", "mc.note LIKE '%(200%)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Germany' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info < '7.0'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2009'], projections = ['title'])
	relations = [cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j6 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j10 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(k, mk, ["id"], ["keyword_id"])
	j12 = Join(it1, mi, ["id"], ["info_type_id"])
	j13 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j14 = Join(ct, mc, ["id"], ["company_type_id"])
	j15 = Join(cn, mc, ["id"], ["company_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15]

	return JoinGraph(relations, joins)

def create_q22c():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code != '[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'episode')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(USA)%'", "mc.note LIKE '%(200%)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Danish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info < '8.5'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title'])
	relations = [cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j6 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j10 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(k, mk, ["id"], ["keyword_id"])
	j12 = Join(it1, mi, ["id"], ["info_type_id"])
	j13 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j14 = Join(ct, mc, ["id"], ["company_type_id"])
	j15 = Join(cn, mc, ["id"], ["company_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15]

	return JoinGraph(relations, joins)

def create_q22d():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code != '[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'episode')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Danish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info < '8.5'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title'])
	relations = [cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j6 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j10 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(k, mk, ["id"], ["keyword_id"])
	j12 = Join(it1, mi, ["id"], ["info_type_id"])
	j13 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j14 = Join(ct, mc, ["id"], ["company_type_id"])
	j15 = Join(cn, mc, ["id"], ["company_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15]

	return JoinGraph(relations, joins)

def create_q23a():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'complete+verified'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code = '[us]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'release dates'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id'], filters = [], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie')"], projections = ['kind'])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id', 'info', 'note'], filters = ["mi.note LIKE '%internet%'", 'mi.info IS NOT NULL', "(mi.info LIKE 'USA:% 199%' OR mi.info LIKE 'USA:% 200%')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [cc, cct1, cn, ct, it1, k, kt, mc, mi, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(t, cc, ["id"], ["movie_id"])
	j5 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j6 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j7 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j10 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j11 = Join(k, mk, ["id"], ["keyword_id"])
	j12 = Join(it1, mi, ["id"], ["info_type_id"])
	j13 = Join(cn, mc, ["id"], ["company_id"])
	j14 = Join(ct, mc, ["id"], ["company_type_id"])
	j15 = Join(cct1, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15]

	return JoinGraph(relations, joins)

def create_q23b():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'complete+verified'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code = '[us]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'release dates'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'nerd' OR k.keyword = 'loner' OR k.keyword = 'alienation' OR k.keyword = 'dignity')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie')"], projections = ['kind'])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id', 'info', 'note'], filters = ["mi.note LIKE '%internet%'", "mi.info LIKE 'USA:% 200%'"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [cc, cct1, cn, ct, it1, k, kt, mc, mi, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(t, cc, ["id"], ["movie_id"])
	j5 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j6 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j7 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j10 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j11 = Join(k, mk, ["id"], ["keyword_id"])
	j12 = Join(it1, mi, ["id"], ["info_type_id"])
	j13 = Join(cn, mc, ["id"], ["company_id"])
	j14 = Join(ct, mc, ["id"], ["company_type_id"])
	j15 = Join(cct1, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15]

	return JoinGraph(relations, joins)

def create_q23c():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'complete+verified'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code = '[us]'"], projections = [])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'release dates'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id'], filters = [], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'tv movie' OR kt.kind = 'video movie' OR kt.kind = 'video game')"], projections = ['kind'])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_type_id', 'movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'movie_id', 'info', 'note'], filters = ["mi.note LIKE '%internet%'", 'mi.info IS NOT NULL', "(mi.info LIKE 'USA:% 199%' OR mi.info LIKE 'USA:% 200%')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 1990'], projections = ['title'])
	relations = [cc, cct1, cn, ct, it1, k, kt, mc, mi, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mc, ["id"], ["movie_id"])
	j4 = Join(t, cc, ["id"], ["movie_id"])
	j5 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j6 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j7 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j10 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j11 = Join(k, mk, ["id"], ["keyword_id"])
	j12 = Join(it1, mi, ["id"], ["info_type_id"])
	j13 = Join(cn, mc, ["id"], ["company_id"])
	j14 = Join(ct, mc, ["id"], ["company_type_id"])
	j15 = Join(cct1, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15]

	return JoinGraph(relations, joins)

def create_q24a():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'release dates'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'hero' OR k.keyword = 'martial-arts' OR k.keyword = 'hand-to-hand-combat')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ['mi.info IS NOT NULL', "(mi.info LIKE 'Japan:%201%' OR mi.info LIKE 'USA:%201%')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%An%'"], projections = ['name'])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2010'], projections = ['title'])
	relations = [an, chn, ci, cn, it, k, mc, mi, mk, n, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(mc, ci, ["movie_id"], ["movie_id"])
	j5 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j6 = Join(mc, mk, ["movie_id"], ["movie_id"])
	j7 = Join(mi, ci, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j9 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j10 = Join(cn, mc, ["id"], ["company_id"])
	j11 = Join(it, mi, ["id"], ["info_type_id"])
	j12 = Join(n, ci, ["id"], ["person_id"])
	j13 = Join(rt, ci, ["id"], ["role_id"])
	j14 = Join(n, an, ["id"], ["person_id"])
	j15 = Join(ci, an, ["person_id"], ["person_id"])
	j16 = Join(chn, ci, ["id"], ["person_role_id"])
	j17 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17]

	return JoinGraph(relations, joins)

def create_q24b():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'country_code', 'id'], filters = ["cn.country_code ='[us]'", "cn.name = 'DreamWorks Animation'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'release dates'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'hero' OR k.keyword = 'martial-arts' OR k.keyword = 'hand-to-hand-combat' OR k.keyword = 'computer-animated-movie')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ['mi.info IS NOT NULL', "(mi.info LIKE 'Japan:%201%' OR mi.info LIKE 'USA:%201%')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%An%'"], projections = ['name'])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2010', "t.title LIKE 'Kung Fu Panda%'"], projections = ['title'])
	relations = [an, chn, ci, cn, it, k, mc, mi, mk, n, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(mc, ci, ["movie_id"], ["movie_id"])
	j5 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j6 = Join(mc, mk, ["movie_id"], ["movie_id"])
	j7 = Join(mi, ci, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j9 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j10 = Join(cn, mc, ["id"], ["company_id"])
	j11 = Join(it, mi, ["id"], ["info_type_id"])
	j12 = Join(n, ci, ["id"], ["person_id"])
	j13 = Join(rt, ci, ["id"], ["role_id"])
	j14 = Join(n, an, ["id"], ["person_id"])
	j15 = Join(ci, an, ["person_id"], ["person_id"])
	j16 = Join(chn, ci, ["id"], ["person_role_id"])
	j17 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17]

	return JoinGraph(relations, joins)

def create_q25a():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity')"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi.info = 'Horror'"], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender = 'm'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [ci, it1, it2, k, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j5 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j7 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j9 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j10 = Join(n, ci, ["id"], ["person_id"])
	j11 = Join(it1, mi, ["id"], ["info_type_id"])
	j12 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j13 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q25b():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity')"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi.info = 'Horror'"], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender = 'm'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2010', "t.title LIKE 'Vampire%'"], projections = ['title'])
	relations = [ci, it1, it2, k, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j5 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j7 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j9 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j10 = Join(n, ci, ["id"], ["person_id"])
	j11 = Join(it1, mi, ["id"], ["info_type_id"])
	j12 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j13 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q25c():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'violence' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity' OR k.keyword = 'hospital')"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Horror' OR mi.info = 'Action' OR mi.info = 'Sci-Fi' OR mi.info = 'Thriller' OR mi.info = 'Crime' OR mi.info = 'War')"], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender = 'm'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [ci, it1, it2, k, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j5 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j7 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j9 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j10 = Join(n, ci, ["id"], ["person_id"])
	j11 = Join(it1, mi, ["id"], ["info_type_id"])
	j12 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j13 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q26a():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind LIKE '%complete%'"], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = ['chn.name IS NOT NULL', "(chn.name LIKE '%man%' OR chn.name LIKE '%Man%')"], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'person_role_id', 'movie_id'], filters = [], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'superhero' OR k.keyword = 'marvel-comics' OR k.keyword = 'based-on-comic' OR k.keyword = 'tv-special' OR k.keyword = 'fight' OR k.keyword = 'violence' OR k.keyword = 'magnet' OR k.keyword = 'web' OR k.keyword = 'claw' OR k.keyword = 'laser')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind = 'movie'"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '7.0'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = [], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [cc, cct1, cct2, chn, ci, it2, k, kt, mi_idx, mk, n, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, cc, ["id"], ["movie_id"])
	j4 = Join(t, mi_idx, ["id"], ["movie_id"])
	j5 = Join(mk, ci, ["movie_id"], ["movie_id"])
	j6 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j9 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j10 = Join(cc, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(chn, ci, ["id"], ["person_role_id"])
	j12 = Join(n, ci, ["id"], ["person_id"])
	j13 = Join(k, mk, ["id"], ["keyword_id"])
	j14 = Join(cct1, cc, ["id"], ["subject_id"])
	j15 = Join(cct2, cc, ["id"], ["status_id"])
	j16 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16]

	return JoinGraph(relations, joins)

def create_q26b():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind LIKE '%complete%'"], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = ['chn.name IS NOT NULL', "(chn.name LIKE '%man%' OR chn.name LIKE '%Man%')"], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'person_role_id', 'movie_id'], filters = [], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'superhero' OR k.keyword = 'marvel-comics' OR k.keyword = 'based-on-comic' OR k.keyword = 'fight')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind = 'movie'"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '8.0'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title'])
	relations = [cc, cct1, cct2, chn, ci, it2, k, kt, mi_idx, mk, n, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, cc, ["id"], ["movie_id"])
	j4 = Join(t, mi_idx, ["id"], ["movie_id"])
	j5 = Join(mk, ci, ["movie_id"], ["movie_id"])
	j6 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j9 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j10 = Join(cc, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(chn, ci, ["id"], ["person_role_id"])
	j12 = Join(n, ci, ["id"], ["person_id"])
	j13 = Join(k, mk, ["id"], ["keyword_id"])
	j14 = Join(cct1, cc, ["id"], ["subject_id"])
	j15 = Join(cct2, cc, ["id"], ["status_id"])
	j16 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16]

	return JoinGraph(relations, joins)

def create_q26c():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind LIKE '%complete%'"], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = ['chn.name IS NOT NULL', "(chn.name LIKE '%man%' OR chn.name LIKE '%Man%')"], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'person_role_id', 'movie_id'], filters = [], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'superhero' OR k.keyword = 'marvel-comics' OR k.keyword = 'based-on-comic' OR k.keyword = 'tv-special' OR k.keyword = 'fight' OR k.keyword = 'violence' OR k.keyword = 'magnet' OR k.keyword = 'web' OR k.keyword = 'claw' OR k.keyword = 'laser')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["kt.kind = 'movie'"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [cc, cct1, cct2, chn, ci, it2, k, kt, mi_idx, mk, n, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, cc, ["id"], ["movie_id"])
	j4 = Join(t, mi_idx, ["id"], ["movie_id"])
	j5 = Join(mk, ci, ["movie_id"], ["movie_id"])
	j6 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j9 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j10 = Join(cc, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(chn, ci, ["id"], ["person_role_id"])
	j12 = Join(n, ci, ["id"], ["person_id"])
	j13 = Join(k, mk, ["id"], ["keyword_id"])
	j14 = Join(cct1, cc, ["id"], ["subject_id"])
	j15 = Join(cct2, cc, ["id"], ["status_id"])
	j16 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16]

	return JoinGraph(relations, joins)

def create_q27a():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["(cct1.kind = 'cast' OR cct1.kind = 'crew')"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind = 'complete'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'", "(cn.name LIKE '%Film%' OR cn.name LIKE '%Warner%')"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='sequel'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link LIKE '%follow%'"], projections = ['link'])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NULL'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Germany' OR mi.info = 'Swedish' OR mi.info = 'German')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 1950', 't.production_year <= 2000'], projections = ['title'])
	relations = [cc, cct1, cct2, cn, ct, k, lt, mc, mi, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(mi, t, ["movie_id"], ["id"])
	j8 = Join(t, cc, ["id"], ["movie_id"])
	j9 = Join(cct1, cc, ["id"], ["subject_id"])
	j10 = Join(cct2, cc, ["id"], ["status_id"])
	j11 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j12 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j13 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j14 = Join(ml, mi, ["movie_id"], ["movie_id"])
	j15 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j16 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j17 = Join(ml, cc, ["movie_id"], ["movie_id"])
	j18 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j19 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j20 = Join(mi, cc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20]

	return JoinGraph(relations, joins)

def create_q27b():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["(cct1.kind = 'cast' OR cct1.kind = 'crew')"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind = 'complete'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'", "(cn.name LIKE '%Film%' OR cn.name LIKE '%Warner%')"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='sequel'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link LIKE '%follow%'"], projections = ['link'])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NULL'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Germany' OR mi.info = 'Swedish' OR mi.info = 'German')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year = 1998'], projections = ['title'])
	relations = [cc, cct1, cct2, cn, ct, k, lt, mc, mi, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(mi, t, ["movie_id"], ["id"])
	j8 = Join(t, cc, ["id"], ["movie_id"])
	j9 = Join(cct1, cc, ["id"], ["subject_id"])
	j10 = Join(cct2, cc, ["id"], ["status_id"])
	j11 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j12 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j13 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j14 = Join(ml, mi, ["movie_id"], ["movie_id"])
	j15 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j16 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j17 = Join(ml, cc, ["movie_id"], ["movie_id"])
	j18 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j19 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j20 = Join(mi, cc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20]

	return JoinGraph(relations, joins)

def create_q27c():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind LIKE 'complete%'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'", "(cn.name LIKE '%Film%' OR cn.name LIKE '%Warner%')"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind ='production companies'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='sequel'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link LIKE '%follow%'"], projections = ['link'])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NULL'], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'English')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 1950', 't.production_year <= 2010'], projections = ['title'])
	relations = [cc, cct1, cct2, cn, ct, k, lt, mc, mi, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(mi, t, ["movie_id"], ["id"])
	j8 = Join(t, cc, ["id"], ["movie_id"])
	j9 = Join(cct1, cc, ["id"], ["subject_id"])
	j10 = Join(cct2, cc, ["id"], ["status_id"])
	j11 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j12 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j13 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j14 = Join(ml, mi, ["movie_id"], ["movie_id"])
	j15 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j16 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j17 = Join(ml, cc, ["movie_id"], ["movie_id"])
	j18 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j19 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j20 = Join(mi, cc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20]

	return JoinGraph(relations, joins)

def create_q28a():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'crew'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind != 'complete+verified'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code != '[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'episode')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(USA)%'", "mc.note LIKE '%(200%)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Danish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info < '8.5'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [cc, cct1, cct2, cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(t, cc, ["id"], ["movie_id"])
	j6 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j12 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j13 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j14 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j15 = Join(mi_idx, cc, ["movie_id"], ["movie_id"])
	j16 = Join(k, mk, ["id"], ["keyword_id"])
	j17 = Join(it1, mi, ["id"], ["info_type_id"])
	j18 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j19 = Join(ct, mc, ["id"], ["company_type_id"])
	j20 = Join(cn, mc, ["id"], ["company_id"])
	j21 = Join(cct1, cc, ["id"], ["subject_id"])
	j22 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20, j21, j22]

	return JoinGraph(relations, joins)

def create_q28b():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'crew'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind != 'complete+verified'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code != '[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'episode')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(USA)%'", "mc.note LIKE '%(200%)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Germany' OR mi.info = 'Swedish' OR mi.info = 'German')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '6.5'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title'])
	relations = [cc, cct1, cct2, cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(t, cc, ["id"], ["movie_id"])
	j6 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j12 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j13 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j14 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j15 = Join(mi_idx, cc, ["movie_id"], ["movie_id"])
	j16 = Join(k, mk, ["id"], ["keyword_id"])
	j17 = Join(it1, mi, ["id"], ["info_type_id"])
	j18 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j19 = Join(ct, mc, ["id"], ["company_type_id"])
	j20 = Join(cn, mc, ["id"], ["company_id"])
	j21 = Join(cct1, cc, ["id"], ["subject_id"])
	j22 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20, j21, j22]

	return JoinGraph(relations, joins)

def create_q28c():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind = 'complete'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code != '[us]'"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'episode')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(USA)%'", "mc.note LIKE '%(200%)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Danish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info < '8.5'"], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title'])
	relations = [cc, cct1, cct2, cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(t, cc, ["id"], ["movie_id"])
	j6 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j12 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j13 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j14 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j15 = Join(mi_idx, cc, ["movie_id"], ["movie_id"])
	j16 = Join(k, mk, ["id"], ["keyword_id"])
	j17 = Join(it1, mi, ["id"], ["info_type_id"])
	j18 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j19 = Join(ct, mc, ["id"], ["company_type_id"])
	j20 = Join(cn, mc, ["id"], ["company_id"])
	j21 = Join(cct1, cc, ["id"], ["subject_id"])
	j22 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20, j21, j22]

	return JoinGraph(relations, joins)

def create_q29a():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind ='cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind ='complete+verified'"], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = ["chn.name = 'Queen'"], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'release dates'"], projections = [])
	it3 = Relation(name = "info_type", alias = "it3", attributes = ['id', 'info'], filters = ["it3.info = 'trivia'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword = 'computer-animation'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ['mi.info IS NOT NULL', "(mi.info LIKE 'Japan:%200%' OR mi.info LIKE 'USA:%200%')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%An%'"], projections = ['name'])
	pi = Relation(name = "person_info", alias = "pi", attributes = ['person_id', 'info_type_id'], filters = [], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ["t.title = 'Shrek 2'", 't.production_year >= 2000', 't.production_year <= 2010'], projections = ['title'])
	relations = [an, cc, cct1, cct2, chn, ci, cn, it, it3, k, mc, mi, mk, n, pi, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(t, cc, ["id"], ["movie_id"])
	j5 = Join(mc, ci, ["movie_id"], ["movie_id"])
	j6 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j7 = Join(mc, mk, ["movie_id"], ["movie_id"])
	j8 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, ci, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j11 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j12 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j13 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j14 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j15 = Join(cn, mc, ["id"], ["company_id"])
	j16 = Join(it, mi, ["id"], ["info_type_id"])
	j17 = Join(n, ci, ["id"], ["person_id"])
	j18 = Join(rt, ci, ["id"], ["role_id"])
	j19 = Join(n, an, ["id"], ["person_id"])
	j20 = Join(ci, an, ["person_id"], ["person_id"])
	j21 = Join(chn, ci, ["id"], ["person_role_id"])
	j22 = Join(n, pi, ["id"], ["person_id"])
	j23 = Join(ci, pi, ["person_id"], ["person_id"])
	j24 = Join(it3, pi, ["id"], ["info_type_id"])
	j25 = Join(k, mk, ["id"], ["keyword_id"])
	j26 = Join(cct1, cc, ["id"], ["subject_id"])
	j27 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20, j21, j22, j23, j24, j25, j26, j27]

	return JoinGraph(relations, joins)

def create_q29b():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind ='cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind ='complete+verified'"], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = ["chn.name = 'Queen'"], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'release dates'"], projections = [])
	it3 = Relation(name = "info_type", alias = "it3", attributes = ['id', 'info'], filters = ["it3.info = 'height'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword = 'computer-animation'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi.info LIKE 'USA:%200%'"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%An%'"], projections = ['name'])
	pi = Relation(name = "person_info", alias = "pi", attributes = ['person_id', 'info_type_id'], filters = [], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ["t.title = 'Shrek 2'", 't.production_year >= 2000', 't.production_year <= 2005'], projections = ['title'])
	relations = [an, cc, cct1, cct2, chn, ci, cn, it, it3, k, mc, mi, mk, n, pi, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(t, cc, ["id"], ["movie_id"])
	j5 = Join(mc, ci, ["movie_id"], ["movie_id"])
	j6 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j7 = Join(mc, mk, ["movie_id"], ["movie_id"])
	j8 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, ci, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j11 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j12 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j13 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j14 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j15 = Join(cn, mc, ["id"], ["company_id"])
	j16 = Join(it, mi, ["id"], ["info_type_id"])
	j17 = Join(n, ci, ["id"], ["person_id"])
	j18 = Join(rt, ci, ["id"], ["role_id"])
	j19 = Join(n, an, ["id"], ["person_id"])
	j20 = Join(ci, an, ["person_id"], ["person_id"])
	j21 = Join(chn, ci, ["id"], ["person_role_id"])
	j22 = Join(n, pi, ["id"], ["person_id"])
	j23 = Join(ci, pi, ["person_id"], ["person_id"])
	j24 = Join(it3, pi, ["id"], ["info_type_id"])
	j25 = Join(k, mk, ["id"], ["keyword_id"])
	j26 = Join(cct1, cc, ["id"], ["subject_id"])
	j27 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20, j21, j22, j23, j24, j25, j26, j27]

	return JoinGraph(relations, joins)

def create_q29c():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id'], filters = [], projections = [])
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind ='cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind ='complete+verified'"], projections = [])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info = 'release dates'"], projections = [])
	it3 = Relation(name = "info_type", alias = "it3", attributes = ['id', 'info'], filters = ["it3.info = 'trivia'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword = 'computer-animation'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ['mi.info IS NOT NULL', "(mi.info LIKE 'Japan:%200%' OR mi.info LIKE 'USA:%200%')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%An%'"], projections = ['name'])
	pi = Relation(name = "person_info", alias = "pi", attributes = ['person_id', 'info_type_id'], filters = [], projections = [])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year >= 2000', 't.production_year <= 2010'], projections = ['title'])
	relations = [an, cc, cct1, cct2, chn, ci, cn, it, it3, k, mc, mi, mk, n, pi, rt, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(t, cc, ["id"], ["movie_id"])
	j5 = Join(mc, ci, ["movie_id"], ["movie_id"])
	j6 = Join(mc, mi, ["movie_id"], ["movie_id"])
	j7 = Join(mc, mk, ["movie_id"], ["movie_id"])
	j8 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, ci, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j11 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j12 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j13 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j14 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j15 = Join(cn, mc, ["id"], ["company_id"])
	j16 = Join(it, mi, ["id"], ["info_type_id"])
	j17 = Join(n, ci, ["id"], ["person_id"])
	j18 = Join(rt, ci, ["id"], ["role_id"])
	j19 = Join(n, an, ["id"], ["person_id"])
	j20 = Join(ci, an, ["person_id"], ["person_id"])
	j21 = Join(chn, ci, ["id"], ["person_role_id"])
	j22 = Join(n, pi, ["id"], ["person_id"])
	j23 = Join(ci, pi, ["person_id"], ["person_id"])
	j24 = Join(it3, pi, ["id"], ["info_type_id"])
	j25 = Join(k, mk, ["id"], ["keyword_id"])
	j26 = Join(cct1, cc, ["id"], ["subject_id"])
	j27 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20, j21, j22, j23, j24, j25, j26, j27]

	return JoinGraph(relations, joins)

def create_q30a():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["(cct1.kind = 'cast' OR cct1.kind = 'crew')"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind ='complete+verified'"], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'violence' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity' OR k.keyword = 'hospital')"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Horror' OR mi.info = 'Thriller')"], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender = 'm'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2000'], projections = ['title'])
	relations = [cc, cct1, cct2, ci, it1, it2, k, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(t, cc, ["id"], ["movie_id"])
	j5 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j6 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j11 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j12 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j13 = Join(mi_idx, cc, ["movie_id"], ["movie_id"])
	j14 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j15 = Join(n, ci, ["id"], ["person_id"])
	j16 = Join(it1, mi, ["id"], ["info_type_id"])
	j17 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j18 = Join(k, mk, ["id"], ["keyword_id"])
	j19 = Join(cct1, cc, ["id"], ["subject_id"])
	j20 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20]

	return JoinGraph(relations, joins)

def create_q30b():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["(cct1.kind = 'cast' OR cct1.kind = 'crew')"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind ='complete+verified'"], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'violence' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity' OR k.keyword = 'hospital')"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Horror' OR mi.info = 'Thriller')"], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender = 'm'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2000', "(t.title LIKE '%Freddy%' OR t.title LIKE '%Jason%' OR t.title LIKE 'Saw%')"], projections = ['title'])
	relations = [cc, cct1, cct2, ci, it1, it2, k, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(t, cc, ["id"], ["movie_id"])
	j5 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j6 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j11 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j12 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j13 = Join(mi_idx, cc, ["movie_id"], ["movie_id"])
	j14 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j15 = Join(n, ci, ["id"], ["person_id"])
	j16 = Join(it1, mi, ["id"], ["info_type_id"])
	j17 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j18 = Join(k, mk, ["id"], ["keyword_id"])
	j19 = Join(cct1, cc, ["id"], ["subject_id"])
	j20 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20]

	return JoinGraph(relations, joins)

def create_q30c():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind ='complete+verified'"], projections = [])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'violence' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity' OR k.keyword = 'hospital')"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Horror' OR mi.info = 'Action' OR mi.info = 'Sci-Fi' OR mi.info = 'Thriller' OR mi.info = 'Crime' OR mi.info = 'War')"], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender = 'm'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [cc, cct1, cct2, ci, it1, it2, k, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(t, cc, ["id"], ["movie_id"])
	j5 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j6 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ci, cc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j11 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j12 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j13 = Join(mi_idx, cc, ["movie_id"], ["movie_id"])
	j14 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j15 = Join(n, ci, ["id"], ["person_id"])
	j16 = Join(it1, mi, ["id"], ["info_type_id"])
	j17 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j18 = Join(k, mk, ["id"], ["keyword_id"])
	j19 = Join(cct1, cc, ["id"], ["subject_id"])
	j20 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20]

	return JoinGraph(relations, joins)

def create_q31a():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id'], filters = ["cn.name LIKE 'Lionsgate%'"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'violence' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity' OR k.keyword = 'hospital')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Horror' OR mi.info = 'Thriller')"], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender = 'm'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [ci, cn, it1, it2, k, mc, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j6 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j11 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j12 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j13 = Join(mi_idx, mc, ["movie_id"], ["movie_id"])
	j14 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j15 = Join(n, ci, ["id"], ["person_id"])
	j16 = Join(it1, mi, ["id"], ["info_type_id"])
	j17 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j18 = Join(k, mk, ["id"], ["keyword_id"])
	j19 = Join(cn, mc, ["id"], ["company_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19]

	return JoinGraph(relations, joins)

def create_q31b():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id'], filters = ["cn.name LIKE 'Lionsgate%'"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'violence' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity' OR k.keyword = 'hospital')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'movie_id', 'note'], filters = ["mc.note LIKE '%(Blu-ray)%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Horror' OR mi.info = 'Thriller')"], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender = 'm'"], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2000', "(t.title LIKE '%Freddy%' OR t.title LIKE '%Jason%' OR t.title LIKE 'Saw%')"], projections = ['title'])
	relations = [ci, cn, it1, it2, k, mc, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j6 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j11 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j12 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j13 = Join(mi_idx, mc, ["movie_id"], ["movie_id"])
	j14 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j15 = Join(n, ci, ["id"], ["person_id"])
	j16 = Join(it1, mi, ["id"], ["info_type_id"])
	j17 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j18 = Join(k, mk, ["id"], ["keyword_id"])
	j19 = Join(cn, mc, ["id"], ["company_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19]

	return JoinGraph(relations, joins)

def create_q31c():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id'], filters = ["cn.name LIKE 'Lionsgate%'"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'violence' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity' OR k.keyword = 'hospital')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Horror' OR mi.info = 'Action' OR mi.info = 'Sci-Fi' OR mi.info = 'Thriller' OR mi.info = 'Crime' OR mi.info = 'War')"], projections = ['info'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id'], filters = [], projections = ['name'])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [ci, cn, it1, it2, k, mc, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j6 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j11 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j12 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j13 = Join(mi_idx, mc, ["movie_id"], ["movie_id"])
	j14 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j15 = Join(n, ci, ["id"], ["person_id"])
	j16 = Join(it1, mi, ["id"], ["info_type_id"])
	j17 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j18 = Join(k, mk, ["id"], ["keyword_id"])
	j19 = Join(cn, mc, ["id"], ["company_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19]

	return JoinGraph(relations, joins)

def create_q32a():
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='10,000-mile-club'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = [], projections = ['link'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['linked_movie_id', 'link_type_id', 'movie_id'], filters = [], projections = [])
	t1 = Relation(name = "title", alias = "t1", attributes = ['id', 'title'], filters = [], projections = ['title'])
	t2 = Relation(name = "title", alias = "t2", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [k, lt, mk, ml, t1, t2]

	j0 = Join(mk, k, ["keyword_id"], ["id"])
	j1 = Join(t1, mk, ["id"], ["movie_id"])
	j2 = Join(ml, t1, ["movie_id"], ["id"])
	j3 = Join(ml, t2, ["linked_movie_id"], ["id"])
	j4 = Join(lt, ml, ["id"], ["link_type_id"])
	j5 = Join(mk, t1, ["movie_id"], ["id"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q32b():
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = [], projections = ['link'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['linked_movie_id', 'link_type_id', 'movie_id'], filters = [], projections = [])
	t1 = Relation(name = "title", alias = "t1", attributes = ['id', 'title'], filters = [], projections = ['title'])
	t2 = Relation(name = "title", alias = "t2", attributes = ['id', 'title'], filters = [], projections = ['title'])
	relations = [k, lt, mk, ml, t1, t2]

	j0 = Join(mk, k, ["keyword_id"], ["id"])
	j1 = Join(t1, mk, ["id"], ["movie_id"])
	j2 = Join(ml, t1, ["movie_id"], ["id"])
	j3 = Join(ml, t2, ["linked_movie_id"], ["id"])
	j4 = Join(lt, ml, ["id"], ["link_type_id"])
	j5 = Join(mk, t1, ["movie_id"], ["id"])
	joins = [j0, j1, j2, j3, j4, j5]

	return JoinGraph(relations, joins)

def create_q33a():
	cn1 = Relation(name = "company_name", alias = "cn1", attributes = ['name', 'id', 'country_code'], filters = ["cn1.country_code = '[us]'"], projections = ['name'])
	cn2 = Relation(name = "company_name", alias = "cn2", attributes = ['name', 'id'], filters = [], projections = ['name'])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'rating'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	kt1 = Relation(name = "kind_type", alias = "kt1", attributes = ['id', 'kind'], filters = ["(kt1.kind = 'tv series')"], projections = [])
	kt2 = Relation(name = "kind_type", alias = "kt2", attributes = ['id', 'kind'], filters = ["(kt2.kind = 'tv series')"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["(lt.link = 'sequel' OR lt.link = 'follows' OR lt.link = 'followed by')"], projections = [])
	mc1 = Relation(name = "movie_companies", alias = "mc1", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mc2 = Relation(name = "movie_companies", alias = "mc2", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi_idx1 = Relation(name = "movie_info_idx", alias = "mi_idx1", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mi_idx2 = Relation(name = "movie_info_idx", alias = "mi_idx2", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx2.info < '3.0'"], projections = ['info'])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['linked_movie_id', 'link_type_id', 'movie_id'], filters = [], projections = [])
	t1 = Relation(name = "title", alias = "t1", attributes = ['kind_id', 'id', 'title'], filters = [], projections = ['title'])
	t2 = Relation(name = "title", alias = "t2", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t2.production_year >= 2005', 't2.production_year <= 2008'], projections = ['title'])
	relations = [cn1, cn2, it1, it2, kt1, kt2, lt, mc1, mc2, mi_idx1, mi_idx2, ml, t1, t2]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(t1, ml, ["id"], ["movie_id"])
	j2 = Join(t2, ml, ["id"], ["linked_movie_id"])
	j3 = Join(it1, mi_idx1, ["id"], ["info_type_id"])
	j4 = Join(t1, mi_idx1, ["id"], ["movie_id"])
	j5 = Join(kt1, t1, ["id"], ["kind_id"])
	j6 = Join(cn1, mc1, ["id"], ["company_id"])
	j7 = Join(t1, mc1, ["id"], ["movie_id"])
	j8 = Join(ml, mi_idx1, ["movie_id"], ["movie_id"])
	j9 = Join(ml, mc1, ["movie_id"], ["movie_id"])
	j10 = Join(mi_idx1, mc1, ["movie_id"], ["movie_id"])
	j11 = Join(it2, mi_idx2, ["id"], ["info_type_id"])
	j12 = Join(t2, mi_idx2, ["id"], ["movie_id"])
	j13 = Join(kt2, t2, ["id"], ["kind_id"])
	j14 = Join(cn2, mc2, ["id"], ["company_id"])
	j15 = Join(t2, mc2, ["id"], ["movie_id"])
	j16 = Join(ml, mi_idx2, ["linked_movie_id"], ["movie_id"])
	j17 = Join(ml, mc2, ["linked_movie_id"], ["movie_id"])
	j18 = Join(mi_idx2, mc2, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18]

	return JoinGraph(relations, joins)

def create_q33b():
	cn1 = Relation(name = "company_name", alias = "cn1", attributes = ['name', 'id', 'country_code'], filters = ["cn1.country_code = '[nl]'"], projections = ['name'])
	cn2 = Relation(name = "company_name", alias = "cn2", attributes = ['name', 'id'], filters = [], projections = ['name'])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'rating'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	kt1 = Relation(name = "kind_type", alias = "kt1", attributes = ['id', 'kind'], filters = ["(kt1.kind = 'tv series')"], projections = [])
	kt2 = Relation(name = "kind_type", alias = "kt2", attributes = ['id', 'kind'], filters = ["(kt2.kind = 'tv series')"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["lt.link LIKE '%follow%'"], projections = [])
	mc1 = Relation(name = "movie_companies", alias = "mc1", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mc2 = Relation(name = "movie_companies", alias = "mc2", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi_idx1 = Relation(name = "movie_info_idx", alias = "mi_idx1", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mi_idx2 = Relation(name = "movie_info_idx", alias = "mi_idx2", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx2.info < '3.0'"], projections = ['info'])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['linked_movie_id', 'link_type_id', 'movie_id'], filters = [], projections = [])
	t1 = Relation(name = "title", alias = "t1", attributes = ['kind_id', 'id', 'title'], filters = [], projections = ['title'])
	t2 = Relation(name = "title", alias = "t2", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t2.production_year = 2007'], projections = ['title'])
	relations = [cn1, cn2, it1, it2, kt1, kt2, lt, mc1, mc2, mi_idx1, mi_idx2, ml, t1, t2]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(t1, ml, ["id"], ["movie_id"])
	j2 = Join(t2, ml, ["id"], ["linked_movie_id"])
	j3 = Join(it1, mi_idx1, ["id"], ["info_type_id"])
	j4 = Join(t1, mi_idx1, ["id"], ["movie_id"])
	j5 = Join(kt1, t1, ["id"], ["kind_id"])
	j6 = Join(cn1, mc1, ["id"], ["company_id"])
	j7 = Join(t1, mc1, ["id"], ["movie_id"])
	j8 = Join(ml, mi_idx1, ["movie_id"], ["movie_id"])
	j9 = Join(ml, mc1, ["movie_id"], ["movie_id"])
	j10 = Join(mi_idx1, mc1, ["movie_id"], ["movie_id"])
	j11 = Join(it2, mi_idx2, ["id"], ["info_type_id"])
	j12 = Join(t2, mi_idx2, ["id"], ["movie_id"])
	j13 = Join(kt2, t2, ["id"], ["kind_id"])
	j14 = Join(cn2, mc2, ["id"], ["company_id"])
	j15 = Join(t2, mc2, ["id"], ["movie_id"])
	j16 = Join(ml, mi_idx2, ["linked_movie_id"], ["movie_id"])
	j17 = Join(ml, mc2, ["linked_movie_id"], ["movie_id"])
	j18 = Join(mi_idx2, mc2, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18]

	return JoinGraph(relations, joins)

def create_q33c():
	cn1 = Relation(name = "company_name", alias = "cn1", attributes = ['name', 'id', 'country_code'], filters = ["cn1.country_code != '[us]'"], projections = ['name'])
	cn2 = Relation(name = "company_name", alias = "cn2", attributes = ['name', 'id'], filters = [], projections = ['name'])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'rating'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	kt1 = Relation(name = "kind_type", alias = "kt1", attributes = ['id', 'kind'], filters = ["(kt1.kind = 'tv series' OR kt1.kind = 'episode')"], projections = [])
	kt2 = Relation(name = "kind_type", alias = "kt2", attributes = ['id', 'kind'], filters = ["(kt2.kind = 'tv series' OR kt2.kind = 'episode')"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["(lt.link = 'sequel' OR lt.link = 'follows' OR lt.link = 'followed by')"], projections = [])
	mc1 = Relation(name = "movie_companies", alias = "mc1", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mc2 = Relation(name = "movie_companies", alias = "mc2", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mi_idx1 = Relation(name = "movie_info_idx", alias = "mi_idx1", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info'])
	mi_idx2 = Relation(name = "movie_info_idx", alias = "mi_idx2", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx2.info < '3.5'"], projections = ['info'])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['linked_movie_id', 'link_type_id', 'movie_id'], filters = [], projections = [])
	t1 = Relation(name = "title", alias = "t1", attributes = ['kind_id', 'id', 'title'], filters = [], projections = ['title'])
	t2 = Relation(name = "title", alias = "t2", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t2.production_year >= 2000', 't2.production_year <= 2010'], projections = ['title'])
	relations = [cn1, cn2, it1, it2, kt1, kt2, lt, mc1, mc2, mi_idx1, mi_idx2, ml, t1, t2]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(t1, ml, ["id"], ["movie_id"])
	j2 = Join(t2, ml, ["id"], ["linked_movie_id"])
	j3 = Join(it1, mi_idx1, ["id"], ["info_type_id"])
	j4 = Join(t1, mi_idx1, ["id"], ["movie_id"])
	j5 = Join(kt1, t1, ["id"], ["kind_id"])
	j6 = Join(cn1, mc1, ["id"], ["company_id"])
	j7 = Join(t1, mc1, ["id"], ["movie_id"])
	j8 = Join(ml, mi_idx1, ["movie_id"], ["movie_id"])
	j9 = Join(ml, mc1, ["movie_id"], ["movie_id"])
	j10 = Join(mi_idx1, mc1, ["movie_id"], ["movie_id"])
	j11 = Join(it2, mi_idx2, ["id"], ["info_type_id"])
	j12 = Join(t2, mi_idx2, ["id"], ["movie_id"])
	j13 = Join(kt2, t2, ["id"], ["kind_id"])
	j14 = Join(cn2, mc2, ["id"], ["company_id"])
	j15 = Join(t2, mc2, ["id"], ["movie_id"])
	j16 = Join(ml, mi_idx2, ["linked_movie_id"], ["movie_id"])
	j17 = Join(ml, mc2, ["linked_movie_id"], ["movie_id"])
	j18 = Join(mi_idx2, mc2, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18]

	return JoinGraph(relations, joins)

########################################################################################################################
# JOB Queries - Post-join
########################################################################################################################
def create_q3c_pj():
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword LIKE '%sequel%'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Denish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 1990'], projections = ['title'])
	relations = [k, mi, mk, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j3 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3]

	return JoinGraph(relations, joins)

def create_q4a_pj():
	it = Relation(name = "info_type", alias = "it", attributes = ['id', 'info'], filters = ["it.info ='rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword LIKE '%sequel%'"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info > '5.0'"], projections = ['info', 'movie_id'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title', 'id'])
	relations = [it, k, mi_idx, mk, t]

	j0 = Join(t, mi_idx, ["id"], ["movie_id"])
	j1 = Join(t, mk, ["id"], ["movie_id"])
	j2 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j3 = Join(k, mk, ["id"], ["keyword_id"])
	j4 = Join(it, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4]

	return JoinGraph(relations, joins)

def create_q9c_pj():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['name', 'person_id'])
	chn = Relation(name = "char_name", alias = "chn", attributes = ['name', 'id'], filters = [], projections = ['name', 'id'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'role_id', 'note', 'person_role_id'], filters = ["(ci.note = '(voice)' OR ci.note = '(voice: Japanese version)' OR ci.note = '(voice) (uncredited)' OR ci.note = '(voice: English version)')"], projections = ['person_id', 'person_role_id', 'movie_id'])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender ='f'", "n.name LIKE '%An%'"], projections = ['name', 'id'])
	rt = Relation(name = "role_type", alias = "rt", attributes = ['role', 'id'], filters = ["rt.role ='actress'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title', 'id'])
	relations = [an, chn, ci, cn, mc, n, rt, t]

	j0 = Join(ci, t, ["movie_id"], ["id"])
	j1 = Join(t, mc, ["id"], ["movie_id"])
	j2 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j3 = Join(mc, cn, ["company_id"], ["id"])
	j4 = Join(ci, rt, ["role_id"], ["id"])
	j5 = Join(n, ci, ["id"], ["person_id"])
	j6 = Join(chn, ci, ["id"], ["person_role_id"])
	j7 = Join(an, n, ["person_id"], ["id"])
	j8 = Join(an, ci, ["person_id"], ["person_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q11c_pj():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code !='[pl]'", "(cn.name LIKE '20th Century Fox%' OR cn.name LIKE 'Twentieth Century Fox%')"], projections = ['name'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id', 'kind'], filters = ["ct.kind != 'production companies'", 'ct.kind IS NOT NULL'], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'sequel' OR k.keyword = 'revenge' OR k.keyword = 'based-on-novel')"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['id'], filters = [], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ['mc.note IS NOT NULL'], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['link_type_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id'], filters = ['t.production_year > 1950'], projections = [])
	relations = [cn, ct, k, lt, mc, mk, ml, t]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(ml, t, ["movie_id"], ["id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(mk, k, ["keyword_id"], ["id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mc, ct, ["company_type_id"], ["id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(ml, mk, ["movie_id"], ["movie_id"])
	j8 = Join(ml, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mk, mc, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9]

	return JoinGraph(relations, joins)

def create_q16b_pj():
	an = Relation(name = "aka_name", alias = "an", attributes = ['person_id', 'name'], filters = [], projections = ['person_id', 'name'])
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id'], filters = [], projections = ['person_id', 'movie_id'])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['country_code', 'id'], filters = ["cn.country_code ='[us]'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["k.keyword ='character-name-in-title'"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['movie_id', 'company_id'], filters = [], projections = [])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title', 'id'])
	relations = [an, ci, cn, k, mc, mk, n, t]

	j0 = Join(an, n, ["person_id"], ["id"])
	j1 = Join(n, ci, ["id"], ["person_id"])
	j2 = Join(ci, t, ["movie_id"], ["id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(mk, k, ["keyword_id"], ["id"])
	j5 = Join(t, mc, ["id"], ["movie_id"])
	j6 = Join(mc, cn, ["company_id"], ["id"])
	j7 = Join(an, ci, ["person_id"], ["person_id"])
	j8 = Join(ci, mc, ["movie_id"], ["movie_id"])
	j9 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j10 = Join(mc, mk, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10]

	return JoinGraph(relations, joins)

def create_q18c_pj():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Horror' OR mi.info = 'Action' OR mi.info = 'Sci-Fi' OR mi.info = 'Thriller' OR mi.info = 'Crime' OR mi.info = 'War')"], projections = ['info', 'movie_id'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info', 'movie_id'])
	n = Relation(name = "name", alias = "n", attributes = ['id', 'gender'], filters = ["n.gender = 'm'"], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['id', 'title'], filters = [], projections = ['title', 'id'])
	relations = [ci, it1, it2, mi, mi_idx, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j4 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j5 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(n, ci, ["id"], ["person_id"])
	j7 = Join(it1, mi, ["id"], ["info_type_id"])
	j8 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8]

	return JoinGraph(relations, joins)

def create_q22c_pj():
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code != '[us]'"], projections = ['name', 'id'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'episode')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(USA)%'", "mc.note LIKE '%(200%)%'"], projections = ['company_id', 'movie_id'])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Danish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info < '8.5'"], projections = ['info', 'movie_id'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title', 'id'])
	relations = [cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j6 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j9 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j10 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(k, mk, ["id"], ["keyword_id"])
	j12 = Join(it1, mi, ["id"], ["info_type_id"])
	j13 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j14 = Join(ct, mc, ["id"], ["company_type_id"])
	j15 = Join(cn, mc, ["id"], ["company_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15]

	return JoinGraph(relations, joins)

def create_q25b_pj():
	ci = Relation(name = "cast_info", alias = "ci", attributes = ['person_id', 'movie_id', 'note'], filters = ["(ci.note = '(writer)' OR ci.note = '(head writer)' OR ci.note = '(written by)' OR ci.note = '(story)' OR ci.note = '(story editor)')"], projections = ['movie_id', 'person_id'])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'genres'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'votes'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'blood' OR k.keyword = 'gore' OR k.keyword = 'death' OR k.keyword = 'female-nudity')"], projections = [])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi.info = 'Horror'"], projections = ['info', 'movie_id'])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info', 'movie_id'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	n = Relation(name = "name", alias = "n", attributes = ['name', 'id', 'gender'], filters = ["n.gender = 'm'"], projections = ['name', 'id'])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'id', 'title'], filters = ['t.production_year > 2010', "t.title LIKE 'Vampire%'"], projections = ['title', 'id'])
	relations = [ci, it1, it2, k, mi, mi_idx, mk, n, t]

	j0 = Join(t, mi, ["id"], ["movie_id"])
	j1 = Join(t, mi_idx, ["id"], ["movie_id"])
	j2 = Join(t, ci, ["id"], ["movie_id"])
	j3 = Join(t, mk, ["id"], ["movie_id"])
	j4 = Join(ci, mi, ["movie_id"], ["movie_id"])
	j5 = Join(ci, mi_idx, ["movie_id"], ["movie_id"])
	j6 = Join(ci, mk, ["movie_id"], ["movie_id"])
	j7 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(mi, mk, ["movie_id"], ["movie_id"])
	j9 = Join(mi_idx, mk, ["movie_id"], ["movie_id"])
	j10 = Join(n, ci, ["id"], ["person_id"])
	j11 = Join(it1, mi, ["id"], ["info_type_id"])
	j12 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j13 = Join(k, mk, ["id"], ["keyword_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13]

	return JoinGraph(relations, joins)

def create_q28c_pj():
	cc = Relation(name = "complete_cast", alias = "cc", attributes = ['status_id', 'subject_id', 'movie_id'], filters = [], projections = [])
	cct1 = Relation(name = "comp_cast_type", alias = "cct1", attributes = ['id', 'kind'], filters = ["cct1.kind = 'cast'"], projections = [])
	cct2 = Relation(name = "comp_cast_type", alias = "cct2", attributes = ['id', 'kind'], filters = ["cct2.kind = 'complete'"], projections = [])
	cn = Relation(name = "company_name", alias = "cn", attributes = ['name', 'id', 'country_code'], filters = ["cn.country_code != '[us]'"], projections = ['name', 'id'])
	ct = Relation(name = "company_type", alias = "ct", attributes = ['id'], filters = [], projections = [])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'countries'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	k = Relation(name = "keyword", alias = "k", attributes = ['id', 'keyword'], filters = ["(k.keyword = 'murder' OR k.keyword = 'murder-in-title' OR k.keyword = 'blood' OR k.keyword = 'violence')"], projections = [])
	kt = Relation(name = "kind_type", alias = "kt", attributes = ['id', 'kind'], filters = ["(kt.kind = 'movie' OR kt.kind = 'episode')"], projections = [])
	mc = Relation(name = "movie_companies", alias = "mc", attributes = ['company_id', 'company_type_id', 'movie_id', 'note'], filters = ["mc.note NOT LIKE '%(USA)%'", "mc.note LIKE '%(200%)%'"], projections = ['company_id', 'movie_id'])
	mi = Relation(name = "movie_info", alias = "mi", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["(mi.info = 'Sweden' OR mi.info = 'Norway' OR mi.info = 'Germany' OR mi.info = 'Denmark' OR mi.info = 'Swedish' OR mi.info = 'Danish' OR mi.info = 'Norwegian' OR mi.info = 'German' OR mi.info = 'USA' OR mi.info = 'American')"], projections = [])
	mi_idx = Relation(name = "movie_info_idx", alias = "mi_idx", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx.info < '8.5'"], projections = ['info', 'movie_id'])
	mk = Relation(name = "movie_keyword", alias = "mk", attributes = ['keyword_id', 'movie_id'], filters = [], projections = [])
	t = Relation(name = "title", alias = "t", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t.production_year > 2005'], projections = ['title', 'id'])
	relations = [cc, cct1, cct2, cn, ct, it1, it2, k, kt, mc, mi, mi_idx, mk, t]

	j0 = Join(kt, t, ["id"], ["kind_id"])
	j1 = Join(t, mi, ["id"], ["movie_id"])
	j2 = Join(t, mk, ["id"], ["movie_id"])
	j3 = Join(t, mi_idx, ["id"], ["movie_id"])
	j4 = Join(t, mc, ["id"], ["movie_id"])
	j5 = Join(t, cc, ["id"], ["movie_id"])
	j6 = Join(mk, mi, ["movie_id"], ["movie_id"])
	j7 = Join(mk, mi_idx, ["movie_id"], ["movie_id"])
	j8 = Join(mk, mc, ["movie_id"], ["movie_id"])
	j9 = Join(mk, cc, ["movie_id"], ["movie_id"])
	j10 = Join(mi, mi_idx, ["movie_id"], ["movie_id"])
	j11 = Join(mi, mc, ["movie_id"], ["movie_id"])
	j12 = Join(mi, cc, ["movie_id"], ["movie_id"])
	j13 = Join(mc, mi_idx, ["movie_id"], ["movie_id"])
	j14 = Join(mc, cc, ["movie_id"], ["movie_id"])
	j15 = Join(mi_idx, cc, ["movie_id"], ["movie_id"])
	j16 = Join(k, mk, ["id"], ["keyword_id"])
	j17 = Join(it1, mi, ["id"], ["info_type_id"])
	j18 = Join(it2, mi_idx, ["id"], ["info_type_id"])
	j19 = Join(ct, mc, ["id"], ["company_type_id"])
	j20 = Join(cn, mc, ["id"], ["company_id"])
	j21 = Join(cct1, cc, ["id"], ["subject_id"])
	j22 = Join(cct2, cc, ["id"], ["status_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18, j19, j20, j21, j22]

	return JoinGraph(relations, joins)

def create_q33c_pj():
	cn1 = Relation(name = "company_name", alias = "cn1", attributes = ['name', 'id', 'country_code'], filters = ["cn1.country_code != '[us]'"], projections = ['name', 'id'])
	cn2 = Relation(name = "company_name", alias = "cn2", attributes = ['name', 'id'], filters = [], projections = ['name', 'id'])
	it1 = Relation(name = "info_type", alias = "it1", attributes = ['id', 'info'], filters = ["it1.info = 'rating'"], projections = [])
	it2 = Relation(name = "info_type", alias = "it2", attributes = ['id', 'info'], filters = ["it2.info = 'rating'"], projections = [])
	kt1 = Relation(name = "kind_type", alias = "kt1", attributes = ['id', 'kind'], filters = ["(kt1.kind = 'tv series' OR kt1.kind = 'episode')"], projections = [])
	kt2 = Relation(name = "kind_type", alias = "kt2", attributes = ['id', 'kind'], filters = ["(kt2.kind = 'tv series' OR kt2.kind = 'episode')"], projections = [])
	lt = Relation(name = "link_type", alias = "lt", attributes = ['link', 'id'], filters = ["(lt.link = 'sequel' OR lt.link = 'follows' OR lt.link = 'followed by')"], projections = [])
	mc1 = Relation(name = "movie_companies", alias = "mc1", attributes = ['movie_id', 'company_id'], filters = [], projections = ['company_id', 'movie_id'])
	mc2 = Relation(name = "movie_companies", alias = "mc2", attributes = ['movie_id', 'company_id'], filters = [], projections = ['company_id', 'movie_id'])
	mi_idx1 = Relation(name = "movie_info_idx", alias = "mi_idx1", attributes = ['info_type_id', 'info', 'movie_id'], filters = [], projections = ['info', 'movie_id'])
	mi_idx2 = Relation(name = "movie_info_idx", alias = "mi_idx2", attributes = ['info_type_id', 'info', 'movie_id'], filters = ["mi_idx2.info < '3.5'"], projections = ['info', 'movie_id'])
	ml = Relation(name = "movie_link", alias = "ml", attributes = ['linked_movie_id', 'link_type_id', 'movie_id'], filters = [], projections = ['linked_movie_id', 'movie_id'])
	t1 = Relation(name = "title", alias = "t1", attributes = ['kind_id', 'id', 'title'], filters = [], projections = ['title', 'id'])
	t2 = Relation(name = "title", alias = "t2", attributes = ['production_year', 'kind_id', 'id', 'title'], filters = ['t2.production_year >= 2000', 't2.production_year <= 2010'], projections = ['title', 'id'])
	relations = [cn1, cn2, it1, it2, kt1, kt2, lt, mc1, mc2, mi_idx1, mi_idx2, ml, t1, t2]

	j0 = Join(lt, ml, ["id"], ["link_type_id"])
	j1 = Join(t1, ml, ["id"], ["movie_id"])
	j2 = Join(t2, ml, ["id"], ["linked_movie_id"])
	j3 = Join(it1, mi_idx1, ["id"], ["info_type_id"])
	j4 = Join(t1, mi_idx1, ["id"], ["movie_id"])
	j5 = Join(kt1, t1, ["id"], ["kind_id"])
	j6 = Join(cn1, mc1, ["id"], ["company_id"])
	j7 = Join(t1, mc1, ["id"], ["movie_id"])
	j8 = Join(ml, mi_idx1, ["movie_id"], ["movie_id"])
	j9 = Join(ml, mc1, ["movie_id"], ["movie_id"])
	j10 = Join(mi_idx1, mc1, ["movie_id"], ["movie_id"])
	j11 = Join(it2, mi_idx2, ["id"], ["info_type_id"])
	j12 = Join(t2, mi_idx2, ["id"], ["movie_id"])
	j13 = Join(kt2, t2, ["id"], ["kind_id"])
	j14 = Join(cn2, mc2, ["id"], ["company_id"])
	j15 = Join(t2, mc2, ["id"], ["movie_id"])
	j16 = Join(ml, mi_idx2, ["linked_movie_id"], ["movie_id"])
	j17 = Join(ml, mc2, ["linked_movie_id"], ["movie_id"])
	j18 = Join(mi_idx2, mc2, ["movie_id"], ["movie_id"])
	joins = [j0, j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14, j15, j16, j17, j18]

	return JoinGraph(relations, joins)
