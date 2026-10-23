# Enterprise Hello World

> **The application is intentionally simple. The delivery lifecycle is not.**

Enterprise Hello World is a deliberately small Flask application used to demonstrate a complete software delivery lifecycle without allowing application complexity to obscure the delivery practices around it.

The project now also includes a small public API surface. This deliberately extends the original lifecycle demonstration without turning the repository into a large application.

## Live demonstration

**Application**  
https://enterprise-hello-world.onrender.com/

**Health endpoint**  
https://enterprise-hello-world.onrender.com/health

**API overview**  
https://enterprise-hello-world.onrender.com/api

**API status**  
https://enterprise-hello-world.onrender.com/api/status

**Projects API**  
https://enterprise-hello-world.onrender.com/api/projects

> **Demo hosting note**
>
> The live demonstration is hosted on Render's free service tier. After a period of inactivity the service may spin down, so the first request can take up to approximately 60 seconds while the instance starts. Subsequent requests should respond normally.
>
> This cold-start delay is expected platform behaviour and does not, by itself, indicate an application incident.

## Application behaviour

### Root

`GET /`

Returns:

```text
Hello World
```

### Health

`GET /health`

```json
{
  "service": "enterprise-hello-world",
  "status": "healthy"
}
```

### API overview

`GET /api`

Returns API metadata and the available API paths.

### API status

`GET /api/status`

Returns the application version, operating state, runtime and hosting platform.

### Projects

`GET /api/projects`

Returns a small set of public engineering projects. It exists to demonstrate a real JSON API response that can be consumed and tested using tools such as Postman.

## Why the API was added

The original application demonstrated a disciplined software-delivery lifecycle around a deliberately simple application.

Version 2 extends the same project into API delivery while preserving the principle:

> **Simple application. Serious delivery discipline.**

This evolution demonstrates:

- incremental application change
- backwards-compatible endpoint design
- REST-style JSON endpoints
- automated API testing
- deployment through the existing GitHub → Render flow
- health and status separation
- external API consumption using Postman
- change documentation and release validation

## What this project demonstrates

- requirements and acceptance criteria
- GitHub Issues and GitHub Projects
- source control and branch-based development
- automated unit testing
- GitHub Actions CI
- security scanning
- Azure Bicep as an Infrastructure as Code reference
- public application deployment
- REST-style API delivery
- Postman API validation
- User Acceptance Testing
- release readiness and cutover
- operational runbooks and monitoring
- hypercare
- defect and incident management
- Post-Incident Review
- BAU handover

## Technology

- Python
- Flask
- Gunicorn
- pytest
- GitHub
- GitHub Actions
- Dependabot
- Bandit
- Bicep
- Render
- Postman

The repository includes an Azure App Service Bicep reference implementation. The current live demonstration environment is hosted on Render.

## Delivery lifecycle

```text
Requirement
    ↓
Design
    ↓
Development
    ↓
Source Control
    ↓
Automated Testing / CI
    ↓
UAT
    ↓
Release Readiness
    ↓
Go-Live
    ↓
Hypercare
    ↓
Incident / Defect Management
    ↓
Post-Incident Review
    ↓
BAU Transition
```

The GitHub Project board tracks this lifecycle using:

```text
Backlog → Ready → In Progress → Review / Test → Ready for Release → Hypercare → Done
```

## Running locally

```bash
git clone https://github.com/rakeshranderia/enterprise-hello-world.git
cd enterprise-hello-world
python -m venv .venv
pip install -r requirements.txt
pip install -r requirements-dev.txt
python -m app
```

Local endpoints:

```text
http://127.0.0.1:5000/
http://127.0.0.1:5000/health
http://127.0.0.1:5000/api
http://127.0.0.1:5000/api/status
http://127.0.0.1:5000/api/projects
```

## Hosted runtime

The live service continues to use:

```text
Branch: main
Runtime: Python 3
Build command: pip install -r requirements.txt
Start command: gunicorn "app:create_app()"
```

No Render configuration change is required for this version.

See [`docs/hosting-and-runtime.md`](docs/hosting-and-runtime.md) for the hosting model and known platform behaviour.

## API validation

A Postman collection is included under:

```text
postman/enterprise-hello-world.postman_collection.json
```

The collection defaults to the live Render base URL and contains requests for:

- root
- health
- API overview
- API status
- projects

## Documentation

Detailed delivery material is maintained under `docs/`, including requirements, architecture, testing, UAT, release readiness, cutover, hypercare, incident review and operational transition.

The documentation is deliberately more extensive than the application itself.

## Delivery principle

> **Simple application. Serious delivery discipline.**

This repository is a demonstration and learning project. The application, infrastructure and operational scenarios are intentionally simplified and should not be treated as production architecture without appropriate design, security, resilience, cost and operational assessment.
