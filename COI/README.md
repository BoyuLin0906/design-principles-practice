# Composition Over Inheritance

## Intent

Prefer building behavior by combining small parts instead of creating deep or specialized class hierarchies.

## Problem

When features are added through inheritance, new combinations often require new subclasses. That makes the model harder to extend because behavior is tied to a growing family tree instead of reusable building blocks.

## Bad Example

The bad example models different speakers with inheritance. It starts simply, but as soon as Bluetooth and voice-assistant support need to be combined, a new subclass is required. Adding more feature combinations would keep growing the hierarchy.

## Refactored Example

The refactored example keeps `Speaker` small and composes it with separate connection and assistant objects. New combinations can be created by wiring different parts together instead of creating more subclasses. That also makes it easier to add future connection types, such as Wi-Fi or wired connections, without changing `Speaker` itself.

## Trade-offs

Composition usually means more objects are created and connected together. That can feel a little more verbose at first, but it keeps behavior more flexible as feature combinations grow.
