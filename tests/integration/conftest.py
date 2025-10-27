# =============================================================================
# Shared pytest setup for integration tests.
# Fixtures provide ready-to-use objects for all tests:
# - app: the real Flask app instance
# - client: in-process API client for calling routes
# - db_conn: connection to the same database the app uses
# =============================================================================


import sqlite3
import pytest


from app import create_app

@pytest.fixture(scope="session")
def flask_app():
    """Create the real Flask app once per test session."""
    flask_app = create_app()
    flask_app.config.update(TESTING=True)
    return flask_app

@pytest.fixture()
def client(flask_app):
    """Provides a test client to call API routes directly."""
    with flask_app.test_client() as c:
        yield c

@pytest.fixture()
def db_conn(flask_app):
    """Connects to the app database for backend verification."""
    settings = flask_app.config["SETTINGS"]
    db_path = getattr(settings, "sqlite_db_path", None)
    assert db_path, "Expected Settings.db_path to exist for integration tests."

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()
