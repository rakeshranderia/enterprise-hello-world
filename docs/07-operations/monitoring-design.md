# Monitoring Design

## Business Service Signal

The service is considered available when:

- `/` returns HTTP 200;
- `/health` returns HTTP 200 and `healthy`.

## Signals

| Signal | Expected | Response |
|---|---|---|
| Root availability | HTTP 200 | Investigate failure |
| Health availability | HTTP 200 | Investigate failure |
| Health status | healthy | Recover/escalate if unhealthy |
| CI | passing | Block merge if failing |

## Principle

Monitor signals that drive action.

A dashboard without ownership or response is not an operational control.
