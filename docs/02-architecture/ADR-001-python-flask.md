# ADR-001 — Use Python Flask

## Status

Accepted

## Context

The project requires a deliberately simple web service so that the focus remains on the delivery lifecycle rather than application complexity.

## Options Considered

### Static HTML

**Benefits**
- simplest implementation;
- minimal dependencies.

**Limitations**
- less useful for demonstrating automated application tests and health endpoints.

### Python Flask

**Benefits**
- small amount of code;
- easy local execution;
- straightforward automated tests;
- health endpoint simple to implement.

**Limitations**
- requires Python dependency management.

### Full Application Framework

**Benefits**
- more enterprise-like structure.

**Limitations**
- unnecessary complexity for the objective.

## Decision

Use Python Flask.

## Consequences

The application remains small while still supporting CI, dependency management, health checks and test automation.
