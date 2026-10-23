from app import create_app


def test_hello_world():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello World"


def test_health():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["status"] == "healthy"
    assert payload["service"] == "enterprise-hello-world"


def test_api_overview():
    app = create_app()
    client = app.test_client()

    response = client.get("/api")
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["service"] == "enterprise-hello-world"
    assert payload["version"] == "2.0"
    assert payload["endpoints"]["status"] == "/api/status"
    assert payload["endpoints"]["projects"] == "/api/projects"


def test_api_status():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/status")
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["status"] == "operational"
    assert payload["hosting"] == "Render"
    assert payload["version"] == "2.0"


def test_api_projects():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/projects")
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["count"] == 2
    assert len(payload["projects"]) == 2
    assert payload["projects"][0]["name"] == "Enterprise Hello World"
