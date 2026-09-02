# Test Cases

## TC-001 — Root Endpoint

**Given** the service is running  
**When** a user requests `/`  
**Then** HTTP 200 is returned  
**And** the body equals `Hello World`.

## TC-002 — Health Endpoint

**Given** the service is running  
**When** monitoring requests `/health`  
**Then** HTTP 200 is returned  
**And** status equals `healthy`.

## TC-003 — Demonstration UAT Defect

**Purpose:** demonstrate defect detection.

**Expected:** `Hello World`  
**Demonstration failure:** `Helo World`

Do not present this as an accidental historical incident. It is a controlled demonstration scenario.
