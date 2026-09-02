# Enterprise Hello World

> **The application is intentionally simple. The delivery lifecycle is not.**

Enterprise Hello World is a deliberately small Python web service used to demonstrate an end-to-end technology delivery lifecycle:

**Idea → Requirement → Backlog → Build → Test → UAT → CI → IaC → Release → Cutover → Hypercare → Incident → PIR → BAU**

The point of this repository is not the complexity of the application. The point is to show how a simple change can be governed, tested, released, supported and improved using practical engineering and delivery controls.

## What the Application Does

The service exposes two endpoints:

- `/` — returns `Hello World`
- `/health` — returns a simple health response

That is all the application needs to do.

## What the Project Demonstrates

- requirements and user stories;
- acceptance criteria and non-functional requirements;
- architecture decision records;
- Git branching and pull-request workflow;
- automated unit testing;
- linting and lightweight security checks;
- CI with GitHub Actions;
- Infrastructure as Code using Azure Bicep;
- UAT planning and evidence;
- release readiness;
- cutover and rollback planning;
- go-live and hypercare;
- operational acceptance;
- BAU handover;
- incident communications;
- post-incident review;
- technical debt and decision logging;
- documentation and user training.

## Repository Structure

```text
enterprise-hello-world/
├── app/                        # Tiny Python web service
├── tests/                      # Automated tests
├── infrastructure/
│   └── bicep/                  # Demonstration Azure IaC
├── docs/
│   ├── 01-discovery/           # Problem, scope, user story, requirements
│   ├── 02-architecture/        # Architecture and ADRs
│   ├── 03-delivery/            # Backlog, DoD, decisions, project board
│   ├── 04-testing/             # Test plan, test cases, UAT
│   ├── 05-release/             # Release readiness, cutover, rollback
│   ├── 06-training/            # User and support guides
│   ├── 07-operations/          # Runbook, monitoring, BAU handover
│   ├── 08-incident/            # Incident update and PIR examples
│   └── 09-lessons/             # Lessons learned
├── .github/
│   ├── workflows/              # CI and IaC validation
│   ├── ISSUE_TEMPLATE/         # Feature / bug templates
│   └── pull_request_template.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
└── README.md
```

## Local Run

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
python -m app
```

Open:

```text
http://127.0.0.1:5000/
```

Health endpoint:

```text
http://127.0.0.1:5000/health
```

## Run Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Delivery Lifecycle

The project documentation is designed to be followed in order:

1. [`Problem Statement`](docs/01-discovery/problem-statement.md)
2. [`Scope & Success Criteria`](docs/01-discovery/scope-and-success.md)
3. [`User Story`](docs/01-discovery/user-story.md)
4. [`Non-Functional Requirements`](docs/01-discovery/non-functional-requirements.md)
5. [`Architecture`](docs/02-architecture/architecture.md)
6. [`Architecture Decision Record`](docs/02-architecture/ADR-001-python-flask.md)
7. [`GitHub Project Setup`](docs/03-delivery/github-project-setup.md)
8. [`Backlog`](docs/03-delivery/backlog.md)
9. [`Definition of Done`](docs/03-delivery/definition-of-done.md)
10. [`Test Plan`](docs/04-testing/test-plan.md)
11. [`UAT Plan`](docs/04-testing/uat-plan.md)
12. [`Release Readiness`](docs/05-release/release-readiness.md)
13. [`Cutover Plan`](docs/05-release/cutover-plan.md)
14. [`Training`](docs/06-training/user-guide.md)
15. [`Operational Runbook`](docs/07-operations/operational-runbook.md)
16. [`Hypercare`](docs/07-operations/hypercare-plan.md)
17. [`Incident Simulation`](docs/08-incident/incident-simulation.md)
18. [`Post-Incident Review`](docs/08-incident/post-incident-review.md)
19. [`BAU Handover`](docs/07-operations/bau-handover.md)
20. [`Lessons Learned`](docs/09-lessons/lessons-learned.md)

## GitHub Demonstration Scenario

This repository intentionally does **not** manufacture history.

Instead, follow [`docs/03-delivery/demo-scenario.md`](docs/03-delivery/demo-scenario.md) to create real:

- issues;
- branches;
- pull requests;
- CI runs;
- an intentional defect;
- a bug fix;
- a release;
- a hypercare incident;
- project-board movement.

That produces an authentic project history.

## Infrastructure as Code

[`infrastructure/bicep/main.bicep`](infrastructure/bicep/main.bicep) defines a small Azure App Service architecture as a demonstration of:

**Desired State → Version Control → Validate → Review → Deploy → Evidence**

The CI workflow validates that the Bicep file can compile. Deployment is intentionally not automatic because this public demonstration repository does not require cloud credentials or paid Azure resources.

## Key Principle

A trivial application can still demonstrate serious delivery discipline.

The value of this repository is the complete operating model around the code:

**Requirement → Delivery → Control → Evidence → Operation → Improvement**
