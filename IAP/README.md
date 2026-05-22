# Invariant Avoidance Principle

## Intent

Design code so it avoids unnecessary rules that different pieces of state must always keep in sync.

## Problem

When one object stores the same information in multiple forms, every change has to update all of them correctly. That creates hidden invariants, and small mistakes can leave the object in an invalid state.

## Bad Example

The bad example stores `items`, `item_count`, and `total_price` inside the same cart. Those values describe the same data from different angles, so every method has to keep them synchronized. One missed update makes the cart inconsistent.

## Refactored Example

The refactored example keeps `items` as the single source of truth and derives the count and total when needed. That removes the synchronization burden and makes the cart harder to corrupt.

## Trade-offs

Deriving values on demand can do a little more work each time they are requested. In small and medium cases, that extra calculation is often a good trade for simpler and safer code.
