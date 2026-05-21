# Law of Demeter

## Intent

Keep objects from reaching too deeply into other objects' internals.

## Problem

When code navigates through long chains of objects, it learns too much about how those objects are built. Small structure changes can then break unrelated parts of the code.

## Bad Example

The bad example makes `ShippingService` reach through `Order`, then `Customer`, then `Address` to prepare a label. The service depends on the internal structure of all three objects.

## Refactored Example

The refactored example asks `Order` for the data the service needs. `Order` and `Customer` hide the navigation details behind small methods, so `ShippingService` only talks to one direct collaborator.

## Trade-offs

Following this principle can add a few forwarding methods. That extra code is usually worth it when it keeps knowledge of object structure in one place.
