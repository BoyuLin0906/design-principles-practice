# Hollywood Principle

## Intent

Use inversion of control so shared workflow code decides when custom behavior runs.

## Problem

Code becomes tightly coupled when the main script directly calls every concrete step in a workflow. As more steps are added, the caller needs to know too much about ordering and implementation details.

## Bad Example

The bad example processes an order by calling inventory, payment, and email services one by one. It works, but the main flow is responsible for every concrete step.

## Refactored Example

The refactored example introduces a workflow object that owns the process and calls registered handlers at the right time. The main script only registers handlers and starts the workflow.

## Trade-offs

The Hollywood Principle can make extension easier, but it also adds indirection. For very small scripts, direct calls may still be simpler.
