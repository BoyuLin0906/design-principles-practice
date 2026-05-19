# Separation of Concerns

## Intent

Split code so each part focuses on a different concern, such as data access, business rules, or presentation.

## Problem

When one class handles request parsing, data creation, notifications, and response formatting, small changes start to affect unrelated areas. That makes the code harder to test and harder to update safely.

## Bad Example

The bad example uses one `OrderController` class to read request data, create the order, send a notification, and build the response. It works, but all concerns are tied together in one place.

## Refactored Example

The refactored example separates the work into a `CreateOrderRequest`, an `OrderService`, a `NotificationService`, and an `OrderResponseBuilder`. `OrderController` coordinates them, so each concern can change more independently.

## Related Principles

Separation of Concerns often supports other design principles too. When concerns are split clearly, it becomes easier to give each class a single responsibility, which aligns with SRP. It also becomes easier to keep interfaces smaller and more focused, which supports ISP.

## Trade-offs

Separating concerns usually means more classes or modules. That can feel a little heavier at first, but it helps when the request format, business rules, notification steps, or response shape needs to change.
