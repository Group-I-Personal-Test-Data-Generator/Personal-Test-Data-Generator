# Unit Tests - Personal Test Data Generator

This directory contains **unit tests** for the `Personal-Test-Data-Generator` backend services.
The tests cover core functionality such as generating CPR numbers, names, addresses, phone numbers, and birthdates.

---

## Table of Contents
1. [Overview](#overview)
2. [Technologies](#technologies)
3. [Test Structure](#test-structure)
4. [Running the Tests](#running-the-tests)
5. [Test Coverage](#test-coverage)
6. [Testing Methodologies](#testing-methodologies)

---

## Overview

The purpose of these tests is to ensure that the backend services in `backend/FakeInfoService/services/fake_info.py` work as expected.
All functions are tested for **valid outputs**, **boundary values**, and **edge cases**.

---

## Technologies

- Python 3.11
- [pytest](https://docs.pytest.org/en/stable/) - testing framework
- [pytest-mock](https://pypi.org/project/pytest-mock/) - for mocking dependencies
- Built-in modules: `random`, `datetime`, `types`, `SimpleNamespace`

---

## Test Structure

### `_load_names()`
- Tests loading names from JSON files.
- Ensures fallback to default names if file is missing.

### `random_gender()`
- Validates that the function always returns `"male"` or `"female"`.

### `make_cpr()`
- Verifies CPR number formatting and gender parity rules.
- Includes **Decision Table Testing (DTT)** and **Boundary Value Analysis (BVA)**.

### `random_name()`
- Ensures first and last names are chosen correctly from lists.
- Handles empty name lists with default values.

### `random_address()`
- Checks structure and values of returned addresses.
- Tests boundary conditions and random branches.

### `random_phone()`
- Validates correct Danish phone number format.
- Ensures only valid prefixes are produced.
- Includes **Equivalence Partitioning (EP)** and **BVA** tests.

### `random_birthdate()`
- Confirms correct year ranges (default and custom).
- Tests boundary years and invalid data types.
- Handles extreme future years gracefully.

---

## Running the Tests

1. Activate your virtual environment:

```bash
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
pip install pytest-mock
```

3. Run all unit tests:

```bash
pytest tests/unit
```

4. For more verbose output:

```bash
pytest -v tests/unit
```

## Test Coverage

The tests ensure:

- Correct data types for all generated values.
- Compliance with business rules (e.g., CPR parity, phone prefixes).
- Proper handling of edge cases and invalid input.
- Robust fallback mechanisms for missing files or empty datasets.

## Testing Methodologies

- Decision Table Testing (DTT): Used for make_cpr parity rules.
- Boundary Value Analysis (BVA): Used for CPR digits, phone numbers, and birthdates.
- Equivalence Partitioning (EP): Used for phone number validation and birthdate ranges.
- Mocking: Used to control random values and database connections for deterministic tests.

All unit tests are designed to be fast, isolated, and reproducible, enabling safe refactoring of core logic without affecting production behavior.
