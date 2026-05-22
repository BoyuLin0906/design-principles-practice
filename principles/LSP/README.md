# Liskov Substitution Principle

## Intent

Subtypes should be usable anywhere their base type is expected.

## Problem

When a subclass changes the expected behavior of a parent class, code that depends on the parent type becomes fragile. The problem is not inheritance by itself. The problem is promising behavior that some subclasses cannot actually support.

## Bad Example

The bad example treats every bird as if it can fly. That works for a sparrow, but a penguin breaks the expectation by raising an error when `fly` is called.

## Refactored Example

The refactored example separates general bird behavior from flying behavior. Code that needs flying depends only on bird types that really support `fly`, so each subtype can be substituted safely.

## Trade-offs

Following LSP often means introducing more focused abstractions instead of one broad parent class. That can add a little structure, but it reduces surprising behavior later.
