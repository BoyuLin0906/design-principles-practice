# Generalization Principle

## Intent

Build solutions that can handle a family of related problems instead of only one narrow case.

## Problem

When code is written for only one exact scenario, small requirement changes often lead to duplicated logic or repeated rewrites. At the same time, excessive generalization can add configuration and abstraction that make simple tasks harder to follow.

## Bad Example

The bad example hardcodes one discount rule for large orders. It works for the current case, but any new threshold or discount rate would likely create another copy of the same logic.

## Refactored Example

The refactored example generalizes the discount calculation with parameters for the threshold and rate. That keeps the code small while making it useful for several related discount rules.
This is a simple form of parameterization: the logic stays the same, but the rule values can change.

## Trade-offs

Generalization is helpful when related variations are real and simple to support. If it grows into many layers, hook points, or abstractions that nobody needs yet, the extra flexibility can become unnecessary complexity.
