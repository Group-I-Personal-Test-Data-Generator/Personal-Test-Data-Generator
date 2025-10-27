from flask import Flask
from flask_cors import CORS

from backend.FakeInfoService.api.routes import api_bp
from backend.FakeInfoService.repositories.settings import Settings
from backend.FakeInfoService.database.initialize import ensure_db_loaded

def create_app() -> Flask:
    settings = Settings.from_env()

    flask_app = Flask(__name__)
    flask_app.config["SETTINGS"] = settings

    # CORS: allow simple GETs from any origin (frontend uses plain fetch)
    CORS(flask_app, resources={r"/*": {"origins": "*"}}, methods=["GET"])

    # ---- IMPORTANT CHANGE: initialize DB here (Flask 3 removed before_first_request)
    ensure_db_loaded(settings)

    # Blueprints
    flask_app.register_blueprint(api_bp)

    @flask_app.errorhandler(400)
    def handle_bad_request(_e):
        return {"error": "Bad request"}, 400

    @flask_app.errorhandler(404)
    def handle_not_found(_e):
        return {"error": "Not found"}, 404

    @flask_app.errorhandler(500)
    def handle_internal_error(_e):
        return {"error": "Internal server error"}, 500

    @flask_app.get("/health")
    def health():
        return {"status": "ok"}, 200

    return flask_app

if __name__ == "__main__":
    app = create_app()
    port = app.config["SETTINGS"].port
    app.run(host="0.0.0.0", port=port, debug=True)
