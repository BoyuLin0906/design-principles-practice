# Principle of Least Astonishment

## Intent

Design code so it behaves the way a reasonable reader expects.

## Problem

Code becomes harder to trust when names suggest one thing but the behavior does something extra. Surprising side effects make bugs easier to introduce because callers cannot predict what a simple operation will change.

## Bad Example

The bad example has a method named `find_by_email`, but it creates and stores a guest user when nothing is found. The caller expects a lookup, yet the method also mutates the store.

## Refactored Example

The refactored example keeps `find_by_email` as a simple lookup that returns `None` when no user exists. A separate `get_or_create_guest` method handles creation, so the behavior is clear from the method name.

## Trade-offs

Making behavior explicit can lead to a few more methods, but the API is easier to understand and safer to use.
