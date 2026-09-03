# Live UAT Record

## Purpose

This document records User Acceptance Testing performed against the live Enterprise Hello World demonstration environment.

## Environment

**Hosting platform:** Render  
**Application:** https://enterprise-hello-world.onrender.com/  
**Health endpoint:** https://enterprise-hello-world.onrender.com/health

## UAT result

**Result: PASS**  
**Date:** 2 September 2026

No release-blocking defects were identified.

## Test 1 — Root endpoint

**Objective:** Confirm the user-facing application meets the agreed Hello World acceptance criterion.

**Request:** `GET /`

**Expected result:** `Hello World`  
**Expected HTTP status:** `200`

**Observed result:** `Hello World`

**Result:** PASS

## Test 2 — Health endpoint

**Objective:** Confirm the deployed service exposes a healthy machine-readable health endpoint.

**Request:** `GET /health`

**Expected result:**

```json
{
  "service": "enterprise-hello-world",
  "status": "healthy"
}
```

**Expected HTTP status:** `200`

**Observed result:**

```json
{
  "service": "enterprise-hello-world",
  "status": "healthy"
}
```

**Result:** PASS

## Hosting observation

The live demonstration is hosted on Render's free service tier.

After a period of inactivity, the first request may take up to approximately 60 seconds while the service starts.

This cold-start behaviour is expected for the demonstration hosting environment and was not treated as a release-blocking defect.

## Outcome

The deployed application meets the current agreed UAT acceptance criteria:

- root endpoint responds successfully
- expected `Hello World` response is returned
- health endpoint responds successfully
- health endpoint reports the service as healthy

The application can proceed to release-readiness activities.

## Evidence

The corresponding GitHub issue should retain the UAT result and project workflow history so the test outcome remains traceable to the delivery lifecycle.
