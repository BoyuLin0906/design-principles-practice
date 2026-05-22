# Open/Closed Principle

## Intent

Software should be open for extension but closed for modification.

## Problem

When one function keeps growing with `if` and `elif` branches for every new case, each change becomes riskier. Adding a new behavior means editing code that already works, which makes regressions more likely.

## Bad Example

The bad example calculates discounts by checking the customer type inside one function. It works for a few cases, but every new discount rule requires changing that same function.

## Refactored Example

The refactored example moves each discount rule into its own class. The checkout flow only depends on a shared interface, so new discount types can be added without changing the calculator itself.

## Trade-offs

Following OCP usually adds a few more classes. That extra structure may feel unnecessary in a tiny script, but it helps once the number of behaviors starts to grow.
