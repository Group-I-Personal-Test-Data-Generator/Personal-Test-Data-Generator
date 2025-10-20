import re

def is_valid_cpr(cpr: str) -> bool:
    return len(cpr) == 10 and cpr.isdigit()

def is_valid_name(name: str) -> bool:
    return len(name) > 0

def is_valid_gender(gender: str) -> bool:
    return gender == "male" or gender == "female"

def is_valid_dob(dob: str) -> bool:
    pattern = r"\d{4}-\d{2}-\d{2}"
    return bool(re.fullmatch(pattern, dob))

def is_valid_street(street: str) -> bool:
    pattern = r"^\D+ \d+"
    return bool(re.match(pattern, street))

def is_valid_town(town: str) -> bool:
    pattern = r"^\d{4} \w+"
    return bool(re.match(pattern, town))

def is_valid_phone_number(phone_number: str) -> bool:
    return len(phone_number) == 8 and phone_number.isdigit()