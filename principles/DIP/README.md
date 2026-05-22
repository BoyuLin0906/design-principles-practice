# Dependency Inversion Principle

## Intent

High-level code should depend on abstractions instead of concrete implementations.

## Problem

When business logic creates and controls specific services directly, it becomes harder to replace those services, test the code, or add alternatives later. A small change in infrastructure can force changes in the higher-level workflow.

## Bad Example

The bad example has `OrderNotifier` depend directly on `EmailService`. It works for email, but the notifier is tightly coupled to that one delivery method.

## Refactored Example

The refactored example introduces a `MessageSender` abstraction. `OrderNotifier` depends on that abstraction, so it can work with `EmailSender`, `SmsSender`, or any future sender with the same contract.

## Trade-offs

Following DIP usually adds an interface or abstract base class. That extra layer can feel unnecessary in a tiny script, but it makes changes easier once the code needs multiple implementations or better testability.
