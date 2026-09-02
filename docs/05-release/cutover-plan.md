# Cutover Plan

## Release

Enterprise Hello World v1.0.0

## Objective

Move the validated application into the agreed target environment.

For the public demonstration, local execution or an optional personal Azure deployment may be used.

## Sequence

| Step | Activity | Validation |
|---|---|---|
| 1 | Confirm release version | Tag/commit correct |
| 2 | Confirm CI green | Workflow passed |
| 3 | Confirm UAT passed | Sign-off recorded |
| 4 | Deploy/start service | Process healthy |
| 5 | Validate `/` | Hello World |
| 6 | Validate `/health` | Healthy |
| 7 | Begin hypercare | Monitoring active |

## Rollback Trigger

Rollback if:

- service fails to start;
- root endpoint fails;
- health endpoint fails;
- material unexpected security/configuration issue is found.

## Rollback

Return to the previous known-good version or stop the demonstration deployment.

## Completion

Cutover completes when:

- core tests pass;
- business validation passes;
- monitoring is healthy;
- no release-blocking issue remains.
