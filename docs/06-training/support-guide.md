# Support Guide

## Quick Health Check

Request:

```text
/health
```

Expected response:

```json
{
  "service": "enterprise-hello-world",
  "status": "healthy"
}
```

## If Root Endpoint Fails

1. Check process/service status.
2. Check health endpoint.
3. Review recent changes.
4. Review CI/release version.
5. Restart/recover if appropriate.
6. Escalate if recovery fails.

## Evidence to Capture

- timestamp;
- error;
- endpoint response;
- version;
- relevant logs;
- action taken.
