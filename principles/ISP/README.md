# Interface Segregation Principle

## Intent

Clients should not be forced to depend on methods they do not use.

## Problem

When one interface tries to cover too many responsibilities, simple classes must implement methods that do not make sense for them. That creates awkward code and often leads to placeholder behavior or runtime errors.

## Bad Example

The bad example uses one `OfficeMachine` interface for printing, scanning, and faxing. A basic printer only needs printing, but it is still forced to define `scan` and `fax`.

## Refactored Example

The refactored example splits the large interface into smaller ones. A basic printer depends only on `Printer`, while a multifunction device can implement the extra interfaces it actually supports.

## Trade-offs

Following ISP may introduce more interfaces or abstract classes. That extra structure can feel unnecessary in very small programs, but it keeps dependencies focused as features grow.
