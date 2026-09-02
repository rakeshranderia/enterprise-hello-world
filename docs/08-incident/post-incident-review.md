# Post-Incident Review — Demonstration

## Incident

Incorrect Hello World response during hypercare.

## Type

Controlled demonstration scenario.

## Impact

The service remained available but failed the primary acceptance criterion.

## Contributing Factor

A deliberately introduced change was used to demonstrate the defect lifecycle.

## Detection

UAT/manual validation identified the incorrect response.

## Recovery

A bug issue was raised and the correct response restored through a branch, pull request and CI validation.

## What Worked

- clear acceptance criterion;
- automated test;
- issue tracking;
- branch/PR workflow;
- controlled release process.

## Improvement

Do not weaken automated tests merely to make a changed result pass.

Tests should protect the requirement, not merely mirror the implementation.

## Action

Keep acceptance criteria, automated tests and UAT aligned.
