#pragma once

#include <concepts>
#include <functional>
#include <iostream>


namespace m {

template<bool Condition, typename T>
struct OptField
{
    private:
    T value_;

    public:
    OptField() = default;

    template<typename U>
    requires std::convertible_to<U, T>
    OptField(U &&value) : value_(std::forward<U>(value)) { }

    operator T&() { return value_; }
    operator const T&() const { return value_; }

    template<typename U>
    requires std::convertible_to<U, T>
    OptField & operator=(U &&value) {
        value_ = T(value);
        return *this;
    }

    T & operator*() { return value_; }
    const T & operator*() const { return value_; }

    T * operator->() { return &value_; }
    const T * operator->() const { return &value_; }

    friend std::ostream & operator<<(std::ostream &out, const OptField &F) { return out << F.value_; }
};

template<typename T>
struct OptField<false,T>
{
    OptField() = default;
    OptField(T) { }
};

}
