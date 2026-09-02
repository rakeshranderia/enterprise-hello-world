# Test Plan

## Objective

Confirm that the service meets functional and basic operational requirements.

## Test Types

### Unit / Automated

Validate:

- root endpoint status;
- Hello World response;
- health endpoint status;
- health payload.

### Manual Functional

Open the root URL and confirm expected output.

### UAT

Confirm the service meets the user story.

### IaC Validation

Compile Bicep to confirm valid syntax.

## Entry Criteria

- code available;
- dependencies install;
- environment starts successfully.

## Exit Criteria

- automated tests pass;
- no critical defects;
- UAT completed;
- material limitations documented.
