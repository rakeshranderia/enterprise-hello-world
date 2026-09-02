# Architecture

## Logical View

```text
User / Monitor
      |
      v
Python Flask Service
   |         |
   |         +--> /health
   |
   +------------> /
```

## Demonstration Azure Target

```text
Internet
   |
 HTTPS
   |
Azure App Service
   |
Python Flask Application
```

## Delivery Components

```text
Developer
   |
Git Branch
   |
Pull Request
   |
GitHub Actions
   |---- Lint
   |---- Unit Tests
   |---- Security Scan
   |
Merge to main
   |
Release Readiness
   |
Git Tag / Release
```

Infrastructure is represented using Bicep and validated separately.

## Design Principles

- intentionally minimal application;
- no customer or employer data;
- no secrets;
- simple recovery;
- documentation stored with code;
- automated validation where practical.
