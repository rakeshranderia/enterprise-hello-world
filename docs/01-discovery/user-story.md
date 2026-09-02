# User Story

## Primary Story

**As a** user  
**I want** to open the service  
**So that** I can see a Hello World response.

## Acceptance Criteria

### Scenario 1 — Hello World

**Given** the service is available  
**When** I open the root URL  
**Then** I receive `Hello World`.

### Scenario 2 — Health

**Given** the service is running  
**When** monitoring calls `/health`  
**Then** the response status is HTTP 200  
**And** the JSON payload reports `healthy`.

## Definition of Done

- acceptance criteria met;
- unit tests pass;
- CI passes;
- documentation updated;
- security checks pass;
- operational readiness confirmed.
