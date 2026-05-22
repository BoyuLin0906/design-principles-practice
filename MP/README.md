# Model Principle

## Intent

Shape the software around the real concepts and actions of the problem domain, so the code mirrors what the system is actually meant to support.

## Problem

When code is organized around convenient data lookups or generic utility actions instead of domain concepts, behavior can work only by accident. That makes changes risky because the code no longer says clearly what is being acted on or why.

## Bad Example

The bad example stores orders as loose dictionaries and removes them by product SKU. That feels convenient at first, but it only works while there happens to be one matching order.

## Refactored Example

The refactored example introduces small `Product` and `Order` objects and removes orders by `order_id`. The code now uses the same concept the business cares about: an order is removed as an order, not as a product.

## Trade-offs

Modeling the domain directly adds a little structure, but it often removes hidden assumptions. The goal is to model what matters, not every detail of the real world.
