# Version 2 Deployment Checklist

## Before commit

- [ ] Read `docs/api-evolution-v2.md`.
- [ ] Replace `app/__init__.py`.
- [ ] Replace `tests/test_app.py`.
- [ ] Replace `README.md`.
- [ ] Replace `docs/hosting-and-runtime.md`.
- [ ] Add `docs/api-evolution-v2.md`.
- [ ] Add `postman/enterprise-hello-world.postman_collection.json`.

## Local validation

From the repository root:

```powershell
python -m pytest
```

Then:

```powershell
python -m app
```

Validate:

```text
http://127.0.0.1:5000/
http://127.0.0.1:5000/health
http://127.0.0.1:5000/api
http://127.0.0.1:5000/api/status
http://127.0.0.1:5000/api/projects
```

## Suggested Git checkpoints

### Commit 1 — application and tests

```text
feat: add public API endpoints to enterprise hello world
```

Files:

- `app/__init__.py`
- `tests/test_app.py`

### Commit 2 — documentation and Postman

```text
docs: document API evolution and Postman validation
```

Files:

- `README.md`
- `docs/hosting-and-runtime.md`
- `docs/api-evolution-v2.md`
- `postman/enterprise-hello-world.postman_collection.json`

## CI

- [ ] Push branch.
- [ ] Confirm existing GitHub Actions CI passes.
- [ ] Confirm security scanning remains green.
- [ ] Review changes before merge.

## Render

No Render configuration change should be required.

Existing configuration remains:

```text
Build command: pip install -r requirements.txt
Start command: gunicorn "app:create_app()"
```

After merge to `main`:

- [ ] Confirm Render starts a deployment.
- [ ] Confirm deployment completes successfully.
- [ ] Allow for free-tier cold start on the first request.

## Live validation

Check:

- [ ] https://enterprise-hello-world.onrender.com/
- [ ] https://enterprise-hello-world.onrender.com/health
- [ ] https://enterprise-hello-world.onrender.com/api
- [ ] https://enterprise-hello-world.onrender.com/api/status
- [ ] https://enterprise-hello-world.onrender.com/api/projects

## Postman

Import:

```text
postman/enterprise-hello-world.postman_collection.json
```

The collection uses:

```text
baseUrl = https://enterprise-hello-world.onrender.com
```

- [ ] Run all five requests.
- [ ] Confirm all tests pass.
- [ ] Only make the Postman collection/workspace public after the Render endpoints are verified.

## Release close-out

- [ ] Update UAT evidence if you want the release captured formally.
- [ ] Update `CHANGELOG.md`.
- [ ] Move the change through the GitHub Project lifecycle.
- [ ] Treat the first period after deployment as lightweight hypercare.
