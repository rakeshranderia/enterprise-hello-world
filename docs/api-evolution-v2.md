# Version 2 — API Evolution

## Objective

Extend Enterprise Hello World from a simple public web application into a small, testable API-enabled application without undermining the project's original purpose.

The application remains deliberately simple. The learning value comes from applying delivery discipline to an incremental change.

## Scope

Version 2 adds three endpoints:

| Endpoint | Purpose |
|---|---|
| `/api` | API metadata and endpoint discovery |
| `/api/status` | Human-readable application status and runtime metadata |
| `/api/projects` | Example structured JSON data representing public engineering projects |

The existing endpoints remain unchanged:

| Endpoint | Purpose |
|---|---|
| `/` | Original Hello World response |
| `/health` | Lightweight health check |

## Design decisions

### Stay with Flask

The project already uses Flask and Gunicorn successfully on Render. Migrating frameworks solely to obtain an API would create unnecessary change and weaken the project's incremental-delivery story.

Flask can expose JSON endpoints cleanly, so the API is added to the existing application.

### Keep `/health` stable

Operational health checks should be predictable and minimal. The existing `/health` contract remains unchanged.

Additional descriptive metadata belongs in `/api/status`.

### Keep the API read-only

No database, authentication or write operations are introduced in this release.

That keeps the scope proportionate while still enabling:

- JSON responses
- endpoint testing
- Postman consumption
- public API demonstration
- external integration later

## Architecture

```text
User / Browser / Postman
          |
          v
   Render Web Service
          |
          v
       Gunicorn
          |
          v
        Flask
      /   |    \
     /    |     \
    /     |      \
   /      |       \
 /health /api  /api/status  /api/projects
```

## Release acceptance criteria

- `/` continues returning HTTP 200 and `Hello World`.
- `/health` continues returning HTTP 200 and `status=healthy`.
- `/api` returns HTTP 200 and identifies version `2.0`.
- `/api/status` returns HTTP 200 and reports `status=operational`.
- `/api/projects` returns HTTP 200 and a non-empty project list.
- All automated tests pass.
- Existing Render build and start commands remain unchanged.
- The Postman collection runs successfully against the live Render URL after deployment.

## Future extensions

Useful later increments include:

1. API versioning such as `/api/v1/...`
2. request IDs and structured logging
3. basic metrics
4. a small authenticated write endpoint
5. persistence
6. containerising the application
7. deployment to a container platform
8. Kubernetes as a separate later-stage evolution

Those should only be added when they serve a learning or engineering objective rather than to inflate the project.
