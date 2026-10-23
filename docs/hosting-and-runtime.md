# Hosting and Runtime

## Purpose

This document describes the live demonstration environment for Enterprise Hello World and records the known hosting behaviour relevant to testing and operations.

## Live environment

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

## Runtime configuration

```text
Branch: main
Runtime: Python 3
Build command: pip install -r requirements.txt
Start command: gunicorn "app:create_app()"
```

No Render runtime or build change is required for the API evolution. The new endpoints are delivered by the existing Flask application factory and therefore use the same Gunicorn start command.

## Known free-tier behaviour

The demonstration environment uses Render's free service tier.

After a period of inactivity, the service may spin down. The first request following inactivity can therefore take up to approximately 60 seconds while the instance starts.

Expected behaviour:

- the first request after inactivity may be delayed
- subsequent requests should respond normally
- a cold-start delay alone should not be treated as an application incident
- once the service has started, `/health` should be checked before escalating an availability or performance issue

## Health and application status

`/health` is the lightweight availability endpoint.

Expected result:

```json
{
  "service": "enterprise-hello-world",
  "status": "healthy"
}
```

`/api/status` is the public application-status endpoint. It intentionally provides a little more context:

```json
{
  "hosting": "Render",
  "runtime": "Flask + Gunicorn",
  "service": "enterprise-hello-world",
  "status": "operational",
  "version": "2.0"
}
```

The separation allows a lightweight health check to remain stable while the public status representation can evolve.

## Infrastructure as Code

The repository also contains an Azure App Service Bicep reference implementation.

The Bicep files demonstrate an Infrastructure as Code pattern but are not currently responsible for the live Render deployment.

- **Render** provides the current public demonstration environment.
- **Bicep / Azure App Service** demonstrates the Infrastructure as Code reference architecture.

## Operational note

A successful platform deployment is not, by itself, sufficient evidence of a successful release.

The deployed service should also be validated through root endpoint validation, health endpoint validation, API endpoint validation, automated tests, UAT, release-readiness checks and post-release monitoring.
