import pytest
import random
from datetime import date
from types import SimpleNamespace

import backend.FakeInfoService.services.fake_info as mod


# ============================================================
#                 _load_names() TESTS
# ============================================================

def test_load_names_with_existing_file(tmp_path):
    """Should correctly load from existing file."""
    data = {"male_first": ["A"], "female_first": ["B"], "last": ["C"]}
    file_path = tmp_path / "names.json"
    file_path.write_text(str(data).replace("'", '"'))
    result = mod._load_names(str(file_path))
    assert result == data

def test_load_names_fallback(monkeypatch):
    """Should fall back to default names when file missing."""
    result = mod._load_names("nonexistent.json")
    assert set(result.keys()) == {"male_first", "female_first", "last"}


# ============================================================
#                 random_gender() TESTS
# ============================================================

def test_random_gender_returns_valid_value():
    """Should always return 'male' or 'female'."""
    g = mod.random_gender()
    assert g in ["male", "female"]


# ============================================================
#                     make_cpr() TESTS
# ============================================================

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

# --- DTT: Decision Table Testing ---

@pytest.mark.parametrize("gender, mocked_digit, expected_parity", [
    ('male', 3, 1),     # male with odd digit -> odd CPR last digit
    ('male', 4, 1),     # male with even digit -> odd CPR last digit
    ('female', 6, 0),   # female with even digit -> even CPR last digit
    ('female', 7, 0),   # female with odd digit -> even CPR last digit
])
def test_make_cpr_desicion_table_parity(mocker, gender, mocked_digit, expected_parity):
    """Ensure parity logic matches gender rule."""
    mocker.patch('random.randrange', return_value=mocked_digit)
    mocker.patch('random.randint', side_effect=[8])
    dob = date(2000, 1, 1)

    cpr = mod.make_cpr(dob, gender)
    last_digit = int(cpr[-1])

    assert len(cpr) == 10  # the length of cpr has to be 10 digits
    # checking if parity matches the expected value
    assert last_digit % 2 == expected_parity  # rest 1 : uneven for mænd, rest 0 : even for kvinder


# --- BVA / EP for CPR ---

@pytest.mark.parametrize("gender,is_odd", [
    ("male", True),
    ("female", False),
])
def test_cpr_gender_digit_rule( gender, is_odd):
    """Boundary test for CPR parity rule."""
    d = date(1999, 1, 1)
    cpr = mod.make_cpr(d, gender)
    last_digit = int(cpr[-1])
    assert (last_digit % 2 == 1) if is_odd else (last_digit % 2 == 0)


# ============================================================
#                   random_name() TESTS
# ============================================================

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


# ============================================================
#                 random_address() TESTS
# ============================================================

def test_random_address_structure(mock_conn):
    """Should return all expected address fields."""
    addr = mod.random_address(mock_conn)
    assert set(addr.keys()) == {"street", "number", "floor", "door", "postal_code", "town_name"}
    assert addr["postal_code"] == "8000"
    assert addr["town_name"] == "Aarhus"

# --- BVA: Boundary Value Analysis ---

def test_random_address_high_random_value(mock_conn, monkeypatch):
    """Test branch where random.random() = 0.8 (no letter/no 'st')."""
    monkeypatch.setattr(random, "random", lambda: 0.8)
    addr = mod.random_address(mock_conn)
    assert addr["number"] == "1"
    assert addr["floor"] == "1."


# ============================================================
#                 random_phone() TESTS
# ============================================================

# --- EP: Equivalence Partitioning ---

def test_random_phone_format_and_prefix():
    """Should generate valid DK phone number."""
    phone = mod.random_phone()
    assert len(phone) == 8
    assert phone[:2] in mod.DK_PHONE_PREFIXES
    assert phone.isdigit()

# --- BVA: Boundary Value Analysis ---

def test_random_phone_never_produces_invalid_prefix():
    """Ensure no invalid prefixes are generated."""
    invalid_prefixes = ['10', '99', '00']
    result = mod.random_phone()
    prefix = result[:2]
    assert prefix not in invalid_prefixes   # makes sure prefix is not a known invalid value

# BVA: BOUNDARY VALUE ANALYSIS (length)
def test_random_phone_boundary_length():
    result = mod.random_phone()
    # Makes sure that length is 8 and is not 7 (just under the boundary) or 9 (just over the boundary)
    assert len(result) == 8
    assert len(result) not in (7, 9)


# ============================================================
#              random_birthdate() TESTS
# ============================================================

# --- EP / BVA ---

def test_random_birthdate_default_range():
    bd = mod.random_birthdate()
    assert 1930 <= bd.year <= date.today().year - 18

def test_random_birthdate_custom_range():
    bd = mod.random_birthdate(2000, 2005)
    assert 2000 <= bd.year <= 2005

def test_random_birthday_boundary_minimum():
    """Test lower boundary of default range."""
    expected_date = date(1930, 1, 1)   # lowest BVA boundary
    result = mod.random_birthdate()
    assert result == expected_date
    assert isinstance(result, date)

def test_random_birthdate_custom_range_start_year():
    """Custom year range boundary test."""
    start_year, end_year = 2000, 2025
    result = mod.random_birthdate(start_year=start_year, end_year=end_year)
    assert start_year <= result.year <= end_year

@pytest.mark.parametrize('invalid_year', ['1990', None, 1.5])
def test_random_birthday_invalid_datatype(invalid_year):
    '''Test invalid datatypes in input parameter raises error.'''
    with pytest.raises((TypeError, ValueError)):
        mod.random_birthdate(start_year=invalid_year, end_year=2000)

def test_random_birthday_extreme_future_year_aaa():
    """Future year beyond supported range should raise."""
    extreme_year = 10000
    with pytest.raises(ValueError):
        mod.random_birthdate(start_year=1930, end_year=extreme_year)

@pytest.mark.parametrize("year", [1929, 1930, 1931])
def test_ransom_birthdate_boundary_values(year):
    """Boundary years should return same year as input."""
    bd = mod.random_birthdate(start_year=year, end_year=year)
    assert bd.year == year
