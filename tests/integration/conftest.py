# =============================================================================
# Shared pytest setup for integration tests.
# Fixtures provide ready-to-use objects for all tests:
# - app: the real Flask app instance
# - client: in-process API client for calling routes
# - db_conn: connection to the same database the app uses
# =============================================================================

import pytest
import sqlite3

from app import create_app

@pytest.fixture(scope="session")
def app():
    """Create the real Flask app once per test session."""
    app = create_app()
    app.config.update(TESTING=True)
    return app

@pytest.fixture()
def client(app):
    """Provides a test client to call API routes directly."""
    with app.test_client() as c:
        yield c

@pytest.fixture()
def db_conn(app):
    """Connects to the app database for backend verification."""
    settings = app.config["SETTINGS"]
    db_path = getattr(settings, "sqlite_db_path", None)
    assert db_path, "Expected Settings.db_path to exist for integration tests."

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()
