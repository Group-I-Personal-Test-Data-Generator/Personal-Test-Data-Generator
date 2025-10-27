
import random
from types import SimpleNamespace
import pytest

import backend.FakeInfoService.services.fake_info as mod


# --- SETTINGS MOCK ---
@pytest.fixture(autouse=True)
def mock_settings(monkeypatch, tmp_path):
    """Ensure _SETTINGS does not access filesystem or env vars."""
    fake_path = tmp_path / "names.json"
    fake_path.write_text('{"male_first":["TestM"],"female_first":["TestF"],"last":["TestL"]}')
    fake_settings = SimpleNamespace(names_json_path=str(fake_path))
    monkeypatch.setattr(mod, "_SETTINGS", fake_settings)
    yield

# --- FAKE DB CONNECTION ---
@pytest.fixture
def mock_conn():
    """Fake DB connection returning a deterministic town."""
    def fake_pick_random_town(_):
        return ("8000", "Aarhus")

    mod.pick_random_town = fake_pick_random_town
    return SimpleNamespace()

# --- DETERMINISTIC RANDOMNESS ---
@pytest.fixture(autouse=True)
def deterministic_random(monkeypatch):
    """Make randomness predictable for repeatable tests."""
    monkeypatch.setattr(random, "choice", lambda seq: seq[0])
    monkeypatch.setattr(random, "randint", lambda a, b: a)
    monkeypatch.setattr(random, "randrange", lambda a, b=None: a if b else 0)
    monkeypatch.setattr(random, "random", lambda: 0.1)
    yield
