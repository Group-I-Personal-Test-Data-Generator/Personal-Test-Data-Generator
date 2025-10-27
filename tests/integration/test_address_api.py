""" terminal: pytest -s tests/integration/test_address_api.py """     

# Expected structure of the Address dataclass returned by /address
EXPECTED_ADDRESS_SCHEMA = {
    "street": str,
    "number": str,
    "floor": (str, type(None)),       # may be None
    "door": (str, type(None)),        # may be None
    "postal_code": str,
    "town_name": str,
}

# Checks that /address returns a valid Address object shape and correct types.
def test_address_endpoint_returns_valid_structure(client):
    response = client.get("/address")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    address_data = response.get_json()

    # Verify that all expected fields exist and match the expected types
    for field, expected_type in EXPECTED_ADDRESS_SCHEMA.items():
        assert field in address_data, f"Missing field '{field}' in response"
        assert isinstance(address_data[field], expected_type), (
            f"Field '{field}' is not of type {expected_type}" )

    # Postal code and address fields should have valid formatting
    assert address_data["postal_code"].isdigit() and len(address_data["postal_code"]) == 4,(
        "Invalid postal code format")
    assert( address_data["street"] and address_data["number"] and address_data["town_name"]
           ), "Street, number, or town_name is empty"

# Confirms that /address returns data that actually exists in the database.
def test_address_endpoint_returns_db_backed_town(client, db_conn):
    response = client.get("/address")
    assert response.status_code == 200

    address_data = response.get_json()

    matching_row = db_conn.execute(
        "SELECT 1 FROM postal_code WHERE postal_code=? AND town_name=? LIMIT 1",
        (address_data["postal_code"], address_data["town_name"]),
    ).fetchone()

    assert matching_row is not None, "Returned address does not exist in the database"
