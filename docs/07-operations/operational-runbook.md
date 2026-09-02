# Operational Runbook

## Service

Enterprise Hello World

## Purpose

Provide a repeatable operational support pattern.

## Service Check

### Root

Expected:

```text
Hello World
```

### Health

Expected:

```json
{
  "service": "enterprise-hello-world",
  "status": "healthy"
}
```

## Routine Validation

- service reachable;
- health endpoint healthy;
- expected release running;
- no open critical incident.

## Recovery

1. confirm impact;
2. check recent changes;
3. restart service where appropriate;
4. roll back to known-good version if required;
5. validate root and health endpoints;
6. record actions.

## Escalation

Escalate if:

- recovery fails;
- repeated failure occurs;
- security concern exists;
- data/integrity concern exists;
- root cause remains unclear after restoration.

## Evidence

Record:

- incident/change reference;
- version;
- timestamps;
- actions;
- validation result.
