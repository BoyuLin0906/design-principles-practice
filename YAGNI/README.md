# You Aren't Gonna Need It

## Intent

Build what is needed now instead of adding features for imagined future requirements.

## Problem

Code becomes harder to read and maintain when it includes extra options, extension points, or workflows that nobody uses yet. Those additions increase complexity before they provide any real value.

## Bad Example

The bad example exports user data, but it already includes support for multiple file formats that the current requirement does not need. The code works, yet a simple CSV export becomes more complicated than necessary.

## Refactored Example

The refactored example only exports CSV because that is the only format needed today. The behavior stays clear, and new abstractions can be added later if another format becomes a real requirement.

## Trade-offs

YAGNI does not mean ignoring likely changes forever. It means waiting until a new requirement is real before paying the cost of extra design and maintenance.
