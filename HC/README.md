# High Cohesion

## Intent

Keep the behavior inside a class closely related to one clear purpose.

## Problem

When one class takes on several unrelated jobs, it becomes harder to understand and change. A small update can affect parts of the class that do not really belong together.

## Bad Example

The bad example puts order data, email sending, and shipping label printing into the same `Order` class. It may feel convenient at first, but the class now mixes unrelated responsibilities.

## Refactored Example

The refactored example keeps `Order` focused on order data and total calculation. Email and shipping behavior move to separate classes, so each part has a clearer purpose.

## Trade-offs

High cohesion often leads to more small classes instead of one large class. That adds a little structure, but it usually makes code easier to maintain as features grow.
