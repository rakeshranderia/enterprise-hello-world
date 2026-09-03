# Hosting and Runtime

## Purpose

This document describes the live demonstration environment for Enterprise Hello World and records the known hosting behaviour relevant to testing and operations.

## Live environment

**Application**  
https://enterprise-hello-world.onrender.com/

**Health endpoint**  
https://enterprise-hello-world.onrender.com/health

## Runtime configuration

```text
Branch: main
Runtime: Python 3
Build command: pip install -r requirements.txt
Start command: gunicorn "app:create_app()"
```

Gunicorn is used for the hosted runtime rather than the Flask development server. The Flask application uses an application factory defined in `app/__init__.py`.

## Known free-tier behaviour

The demonstration environment uses Render's free service tier.

After a period of inactivity, the service may spin down. The first request following inactivity can therefore take up to approximately 60 seconds while the instance starts.

Expected behaviour:

- the first request after inactivity may be delayed
- subsequent requests should respond normally
- a cold-start delay alone should not be treated as an application incident
- once the service has started, `/health` should be checked before escalating an availability or performance issue

## Health validation

Expected `GET /health` result:

```json
{
  "service": "enterprise-hello-world",
  "status": "healthy"
}
```

Expected HTTP status: `200`

## Infrastructure as Code

The repository also contains an Azure App Service Bicep reference implementation.

The Bicep files demonstrate an Infrastructure as Code pattern but are not currently responsible for the live Render deployment.

- **Render** provides the current public demonstration environment.
- **Bicep / Azure App Service** demonstrates the Infrastructure as Code reference architecture.

## Operational note

A successful platform deployment is not, by itself, sufficient evidence of a successful release.

The deployed service should also be validated through root endpoint validation, health endpoint validation, UAT, release-readiness checks and post-release monitoring.
