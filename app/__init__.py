from flask import Flask, jsonify


PROJECTS = [
    {
        "name": "Enterprise Hello World",
        "type": "application-delivery",
        "status": "live",
        "repository": (
            "https://github.com/rakeshranderia/"
            "enterprise-hello-world"
        ),
        "url": "https://enterprise-hello-world.onrender.com/",
    },
    {
        "name": "Docker Engineering",
        "type": "container-engineering",
        "status": "live",
        "repository": (
            "https://github.com/rakeshranderia/"
            "docker-engineering"
        ),
        "url": (
            "https://rakeshranderia.com.au/"
            "projects/docker-engineering/"
        ),
    },
]


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def hello():
        return "Hello World", 200

    @app.get("/health")
    def health():
        return jsonify(
            status="healthy",
            service="enterprise-hello-world",
        ), 200

    @app.get("/api")
    def api_overview():
        return jsonify(
            service="enterprise-hello-world",
            version="2.0",
            description=(
                "A small public API surface extending the "
                "Enterprise Hello World delivery lifecycle "
                "demonstration."
            ),
            endpoints={
                "health": "/health",
                "status": "/api/status",
                "projects": "/api/projects",
            },
        ), 200

    @app.get("/api/status")
    def api_status():
        return jsonify(
            service="enterprise-hello-world",
            status="operational",
            version="2.0",
            runtime="Flask + Gunicorn",
            hosting="Render",
        ), 200

    @app.get("/api/projects")
    def api_projects():
        return jsonify(
            count=len(PROJECTS),
            projects=PROJECTS,
        ), 200

    return app
