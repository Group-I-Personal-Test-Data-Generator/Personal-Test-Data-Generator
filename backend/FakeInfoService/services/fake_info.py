from __future__ import annotations
import json
import os
import random
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Any, Dict, List, Optional, Tuple

from ..repositories.settings import Settings
from ..repositories.towns_repository import pick_random_town

# Names cache loaded at import time based on env path (via Settings)
_SETTINGS = Settings.from_env()


def _load_names(path: str) -> Dict[str, List[str]]:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            male = data.get("male_first") or data.get("male") or []
            female = data.get("female_first") or data.get("female") or []
            last = data.get("last") or data.get("surnames") or []
            if male and female and last:
                return {"male_first": male, "female_first": female, "last": last}
    return {
        "male_first": ["Lars", "Mikkel", "Anders", "Henrik"],
        "female_first": ["Anna", "Sofie", "Mette", "Ida"],
        "last": ["Nielsen", "Jensen", "Hansen", "Pedersen", "Andersen"],
    }

NAMES = _load_names(_SETTINGS.names_json_path)

DK_PHONE_PREFIXES = [
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
    "30", "31", "40", "41", "42", "50", "51", "52", "53", "60",
    "61", "71", "81", "91", "92", "93"
]

STREET_STEMS = [
    "Birke", "Ege", "Linde", "Fyrre", "Gran", "Ahorn", "Kastanje", "Elme",
    "Sønder", "Nørre", "Øster", "Vester", "Konge", "Kirk", "Skole", "Å"
]
STREET_SUFFIXES = ["vej", "gade", "alle", "plads", "bakke", "parken"]
DOOR_OPTIONS = ["tv", "th", "mf"]


@dataclass
class Address:
    street: str
    number: str
    floor: Optional[str]
    door: Optional[str]
    postal_code: str
    town_name: str


@dataclass
class Person:
    CPR: str
    firstName: str
    lastName: str
    gender: str
    birthDate: str
    address: Address
    phoneNumber: str


def random_gender() -> str:
    return random.choice(["male", "female"])


def random_birthdate(start_year: int = 1930, end_year: Optional[int] = None) -> date:
    from datetime import date as _date
    if end_year is None:
        end_year = _date.today().year - 18
    start = _date(start_year, 1, 1)
    end = _date(end_year, 12, 31)
    d = start + timedelta(days=random.randint(0, (end - start).days))
    return d


def make_cpr(d: date, gender: str) -> str:
    ddmmyy = d.strftime("%d%m%y")
    first_three = f"{random.randint(0, 999):03d}"
    last_digit = random.randrange(0, 10)
    if gender == "male" and last_digit % 2 == 0:
        last_digit += 1
    if gender == "female" and last_digit % 2 == 1:
        last_digit -= 1
    return ddmmyy + first_three + str(last_digit)


def random_name(gender: str) -> Tuple[str, str]:
    if gender == "male":
        first = random.choice(NAMES["male_first"]) if NAMES["male_first"] else "Lars"
    else:
        first = random.choice(NAMES["female_first"]) if NAMES["female_first"] else "Anna"
    last = random.choice(NAMES["last"]) if NAMES["last"] else "Nielsen"
    return first, last


def random_phone() -> str:
    prefix = random.choice(DK_PHONE_PREFIXES)
    rest = f"{random.randint(0, 9999999):07d}"
    return prefix + rest


def random_address(conn) -> Dict[str, Any]:
    street = random.choice(STREET_STEMS) + random.choice(STREET_SUFFIXES)
    number = str(random.randint(1, 199))
    if random.random() < 0.3:
        number += random.choice(list("ABCDEFGH"))
    if random.random() < 0.25:
        floor: Optional[str] = "st."
    else:
        floor = f"{random.randint(1, 5)}."
    if random.random() < 0.2:
        floor = None
    if random.random() < 0.6:
        door: Optional[str] = random.choice(DOOR_OPTIONS)
    else:
        door = str(random.randint(1, 50))
    if floor is None and random.random() < 0.7:
        door = None

    postal_code, town_name = pick_random_town(conn)
    return {
        "street": street,
        "number": number,
        "floor": floor,
        "door": door,
        "postal_code": str(postal_code),
        "town_name": town_name,
    }


def build_person(conn) -> Dict[str, Any]:
    gender = random_gender()
    dob = random_birthdate()
    first, last = random_name(gender)
    return {
        "CPR": make_cpr(dob, gender),
        "firstName": first,
        "lastName": last,
        "gender": gender,
        "birthDate": dob.isoformat(),
        "address": random_address(conn),
        "phoneNumber": random_phone(),
    }
