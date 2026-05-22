# Uniformity Principle

## Intent

Design related code so it follows the same patterns for naming, inputs, and outputs.

## Problem

When similar methods return different shapes or expect different kinds of arguments, callers have to remember special cases. That makes the code slower to read and easier to misuse.

## Bad Example

The bad example has pricing methods that all describe parts of the same checkout calculation, but each one returns data in a different format. The caller has to unpack a float, a dictionary, and a string before it can compute the total.

## Refactored Example

The refactored example keeps the pricing methods uniform by returning `float` values for each amount. The caller can combine the results directly because each method follows the same contract.

## Trade-offs

Uniform APIs can feel a little stricter because they push related code toward one shared shape. That trade-off is usually worth it when the methods represent the same kind of concept.
