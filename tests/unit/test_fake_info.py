import pytest
import random
import builtins
from datetime import date
from types import SimpleNamespace

import backend.FakeInfoService.services.fake_info as mod

# --- Fixtures & Mocks ---

@pytest.fixture
def mock_conn():
    """Fake DB connection returning a deterministic town."""
    def fake_pick_random_town(_):
        return ("8000", "Aarhus")
    mod.pick_random_town = fake_pick_random_town
    return SimpleNamespace()

@pytest.fixture(autouse=True)
def deterministic_random(monkeypatch):
    """Make randomness predictable for repeatable tests."""
    monkeypatch.setattr(random, "choice", lambda seq: seq[0])
    monkeypatch.setattr(random, "randint", lambda a, b: a)
    monkeypatch.setattr(random, "randrange", lambda a, b=None: a if b else 0)
    monkeypatch.setattr(random, "random", lambda: 0.1)
    yield


# --- Tests for _load_names() ---

def test_load_names_with_existing_file(tmp_path):
    data = {"male_first": ["A"], "female_first": ["B"], "last": ["C"]}
    file_path = tmp_path / "names.json"
    file_path.write_text(str(data).replace("'", '"'))
    result = mod._load_names(str(file_path))
    assert result == {"male_first": ["A"], "female_first": ["B"], "last": ["C"]}

def test_load_names_fallback(monkeypatch):
    """Branch where file doesn't exist → default names returned"""
    result = mod._load_names("nonexistent.json")
    assert "male_first" in result and "female_first" in result and "last" in result

# Code coverage 100% for branch and statement with fallback function

# --- random_gender() ---

def test_random_gender_returns_valid_value():
    g = mod.random_gender()
    assert g in ["male", "female"]

# Statement and branch coverage 100% - no branches

# --- random_birthdate() ---

def test_random_birthdate_default_range():
    bd = mod.random_birthdate()
    assert 1930 <= bd.year <= date.today().year - 18

def test_random_birthdate_custom_range():
    bd = mod.random_birthdate(2000, 2005)
    assert 2000 <= bd.year <= 2005

# 100% coverage - possible boundary test missing regarding leap year

# --- make_cpr() ---

def test_make_cpr_male_has_odd_last_digit():
    d = date(2000, 1, 1)
    cpr = mod.make_cpr(d, "male")
    assert cpr[:6] == "010100"
    assert int(cpr[-1]) % 2 == 1

def test_make_cpr_female_has_even_last_digit():
    d = date(1990, 12, 31)
    cpr = mod.make_cpr(d, "female")
    assert cpr[:6] == "311290"
    assert int(cpr[-1]) % 2 == 0

# 

# --- random_name() ---

def test_random_name_male_returns_from_list():
    first, last = mod.random_name("male")
    assert first in mod.NAMES["male_first"]
    assert last in mod.NAMES["last"]

def test_random_name_female_returns_from_list():
    first, last = mod.random_name("female")
    assert first in mod.NAMES["female_first"]
    assert last in mod.NAMES["last"]

def test_random_name_with_empty_lists(monkeypatch):
    monkeypatch.setattr(mod, "NAMES", {"male_first": [], "female_first": [], "last": []})
    f, l = mod.random_name("male")
    assert f == "Lars" and l == "Nielsen"


# --- random_phone() ---

def test_random_phone_format_and_prefix():
    phone = mod.random_phone()
    assert len(phone) == 8
    assert phone[:2] in mod.DK_PHONE_PREFIXES
    assert phone.isdigit()


# --- random_address() ---

def test_random_address_structure(mock_conn):
    addr = mod.random_address(mock_conn)
    assert set(addr.keys()) == {"street", "number", "floor", "door", "postal_code", "town_name"}
    assert addr["postal_code"] == "8000"
    assert addr["town_name"] == "Aarhus"


# --- build_person() ---

def test_build_person_integrated(mock_conn):
    p = mod.build_person(mock_conn)
    assert set(p.keys()) == {
        "CPR", "firstName", "lastName", "gender",
        "birthDate", "address", "phoneNumber"
    }
    assert len(p["CPR"]) == 10
    assert p["address"]["postal_code"] == "8000"
    assert p["gender"] in ["male", "female"]
    assert p["phoneNumber"].isdigit()


# --- Boundary / Equivalence Tests ---

@pytest.mark.parametrize("year", [1929, 1930, 1931])
def test_birthdate_boundary_values(monkeypatch, year):
    bd = mod.random_birthdate(start_year=year, end_year=year)
    assert bd.year == year

@pytest.mark.parametrize("gender,last_digit", [
    ("male", 1),
    ("female", 0)
])
def test_cpr_gender_digit_rule(monkeypatch, gender, last_digit):
    """Decision table: male→odd, female→even"""
    d = date(1999, 1, 1)
    cpr = mod.make_cpr(d, gender)
    assert int(cpr[-1]) % 2 == last_digit % 2
