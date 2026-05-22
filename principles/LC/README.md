# Low Coupling

## Intent

Keep parts of the system connected through as few direct dependencies as practical.

## Problem

When one class directly depends on concrete implementations, small changes can spread across the codebase. The class becomes harder to test, reuse, or extend because it is tied to specific details.

## Bad Example

The bad example makes `OrderService` create `MySQLDatabase` and `EmailSender` by itself. That ties the service to one storage choice and one notification method.

## Refactored Example

The refactored example gives `OrderService` its repository and notifier from the outside. That keeps the service loosely connected to its collaborators, so the notification method can change from email to SMS without changing the service itself.

## Trade-offs

Reducing coupling often adds a little setup code because objects are wired together from the outside. That extra structure can feel unnecessary in a tiny example, but it keeps changes more local as the system grows.
