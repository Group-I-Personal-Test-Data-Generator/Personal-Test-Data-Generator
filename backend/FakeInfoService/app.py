from flask import Flask
from flask_cors import CORS

from database.initialize import ensure_db_loaded
from repositories.settings import Settings
from api.routes import api_bp

def create_app() -> Flask:
    settings = Settings.from_env()

    app = Flask(__name__)
    app.config["SETTINGS"] = settings

    # CORS: allow simple GETs from any origin (frontend uses plain fetch)
    CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET"])

    # ---- IMPORTANT CHANGE: initialize DB here (Flask 3 removed before_first_request)
    ensure_db_loaded(settings)

    # Blueprints
    app.register_blueprint(api_bp)

    @app.get("/health")
    def health():
        return {"status": "ok"}, 200

    return app

if __name__ == "__main__":
    app = create_app()
    port = app.config["SETTINGS"].port
    app.run(host="0.0.0.0", port=port, debug=True)
