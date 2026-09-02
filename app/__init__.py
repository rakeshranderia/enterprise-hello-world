from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def hello():
        return "Hello Wrld", 200

    @app.get("/health")
    def health():
        return jsonify(status="healthy", service="enterprise-hello-world"), 200

    return app
