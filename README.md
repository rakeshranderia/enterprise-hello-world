# Enterprise Hello World

> **The application is intentionally simple. The delivery lifecycle is not.**

Enterprise Hello World is a deliberately small Flask application used to demonstrate a complete software delivery lifecycle without allowing application complexity to obscure the delivery practices around it.

The application itself does two things:

- `/` returns `Hello World`
- `/health` returns a simple JSON health response

The surrounding repository demonstrates requirements, source control, automated testing, CI, Infrastructure as Code, UAT, release governance, operational readiness, hypercare, incident handling and BAU transition.

## Live demonstration

**Application**  
https://enterprise-hello-world.onrender.com/

**Health endpoint**  
https://enterprise-hello-world.onrender.com/health

> **Demo hosting note**
>
> The live demonstration is hosted on Render's free service tier. After a period of inactivity the service may spin down, so the first request can take up to approximately 60 seconds while the instance starts. Subsequent requests should respond normally.
>
> This cold-start delay is expected platform behaviour and does not, by itself, indicate an application incident.

## What this project demonstrates

- requirements and acceptance criteria
- GitHub Issues and GitHub Projects
- source control and branch-based development
- automated unit testing
- GitHub Actions CI
- security scanning
- Azure Bicep as an Infrastructure as Code reference
- public application deployment
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

The repository includes an Azure App Service Bicep reference implementation. The current live demonstration environment is hosted on Render.

## Application behaviour

### Root endpoint

```text
GET /
```

Expected result:

```text
Hello World
```

Expected HTTP status: `200`

### Health endpoint

```text
GET /health
```

Expected result:

```json
{
  "service": "enterprise-hello-world",
  "status": "healthy"
}
```

Expected HTTP status: `200`

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

## Current status

The engineering baseline has been completed:

- acceptance criteria defined
- Hello World endpoint implemented
- health endpoint implemented
- automated unit tests implemented
- CI workflow implemented
- security scanning implemented
- Infrastructure as Code reference created
- public demonstration environment deployed

UAT has been executed successfully against the live Render environment. Release-readiness activities follow next.

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
```

## Hosted runtime

The live service currently uses:

```text
Branch: main
Runtime: Python 3
Build command: pip install -r requirements.txt
Start command: gunicorn "app:create_app()"
```

See [`docs/hosting-and-runtime.md`](docs/hosting-and-runtime.md) for the hosting model and known platform behaviour.

## UAT

The deployed service is validated against the agreed acceptance criteria:

- `/` returns HTTP 200 and `Hello World`
- `/health` returns HTTP 200 and reports `status: healthy`

See [`docs/live-uat.md`](docs/live-uat.md) for the current UAT record.

## Documentation

Detailed delivery material is maintained under `docs/`, including requirements, architecture, testing, UAT, release readiness, cutover, hypercare, incident review and operational transition.

The documentation is deliberately more extensive than the application itself.

## Delivery principle

> **Simple application. Serious delivery discipline.**

This repository is a demonstration and learning project. The application, infrastructure and operational scenarios are intentionally simplified and should not be treated as production architecture without appropriate design, security, resilience, cost and operational assessment.
