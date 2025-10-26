# terminal: pytest -s tests/integration/test_person_api.py

# Expected structure of the dataclass Person object returned by /person
EXPECTED_PERSON_SCHEMA = {
    "cpr": str,
    "first_name": str,
    "last_name": str,
    "gender": str,
    "birth_date": str,
    "address": dict,
    "phone_number": str,
}

# Expected structure of the nested dataclass Address inside Person
EXPECTED_ADDRESS_SCHEMA = {
    "street": str,
    "number": str,
    "floor": (str, type(None)),       # may be None
    "door": (str, type(None)),        # may be None
    "postal_code": str,
    "town_name": str,
}

# Checks that /person returns a valid Person shape and correct types.
def test_person_endpoint_returns_valid_structure(client):
    response = client.get("/person")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    person_data = response.get_json()
    assert isinstance(person_data, dict), "Response is not a JSON object"

    # Person fields
    for field, expected_type in EXPECTED_PERSON_SCHEMA.items():
        assert field in person_data, f"Missing field '{field}' in response"
        assert isinstance(person_data[field], expected_type), f"Field '{field}' is not of type {expected_type}"

    # Address fields
    address = person_data["address"]
    for field, expected_type in EXPECTED_ADDRESS_SCHEMA.items():
        assert field in address, f"Missing field '{field}' in address"
        assert isinstance(address[field], expected_type), f"Field '{field}' is not of type {expected_type}"

    # Format check: basic field sanity
    assert person_data["cpr"].isdigit() and len(person_data["cpr"]) == 10, "Invalid CPR format"
    assert person_data["phone_number"].isdigit() and len(person_data["phone_number"]) == 8, "Invalid phone number format"
    assert address["postal_code"].isdigit() and len(address["postal_code"]) == 4, "Invalid postal code format"
    assert address["street"] and address["number"] and address["town_name"], "Street, number, or town_name is empty"

# Confirms that /person returns an address that exists in the database.
def test_person_endpoint_returns_db_backed_town(client, db_conn):
    response = client.get("/person")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    person_data = response.get_json()
    address = person_data["address"]

    matching_row = db_conn.execute(
        "SELECT 1 FROM postal_code WHERE postal_code=? AND town_name=? LIMIT 1",
        (address["postal_code"], address["town_name"]),
    ).fetchone()

    assert matching_row is not None, "Returned address does not exist in the database"

# Checks that /person handles invalid 'n' query params (type and bounds).
def test_person_endpoint_handles_invalid_params(client):
    assert client.get("/person?n=abc").status_code == 400, "Expected 400 for non-integer 'n'"
    assert client.get("/person?n=0").status_code == 400, "Expected 400 for 'n' less than 1"
    assert client.get("/person?n=101").status_code == 400, "Expected 400 for 'n' greater than 100"
