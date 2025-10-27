from __future__ import annotations
from flask import Blueprint, current_app, jsonify, request
from backend.FakeInfoService.repositories.settings import get_conn
from backend.FakeInfoService.services.fake_info import (
    build_person, random_gender, random_birthdate,
    make_cpr, random_name, random_phone, random_address
)

api_bp = Blueprint("api", __name__)


def _json(obj, status=200):
    return current_app.response_class(
        response=jsonify(obj).get_data(as_text=True),
        status=status,
        mimetype="application/json; charset=utf-8",
    )

def format_person(person: dict) -> dict:
    """Convert snake_case keys to camelCase and match Postman expectations."""
    return {
        "CPR": person.get("cpr"),
        "firstName": person.get("first_name"),
        "lastName": person.get("last_name"),
        "gender": person.get("gender"),
        "birthDate": person.get("birth_date"),
        "address": {
            "street": person["address"].get("street"),
            "number": person["address"].get("number"),
            "floor": person["address"].get("floor"),
            "door": person["address"].get("door"),
            "postal_code": person["address"].get("postal_code"),
            "town_name": person["address"].get("town_name"),
        } if person.get("address") else None,
        "phoneNumber": person.get("phone_number"),
    }

@api_bp.get("/person")
def person():
    n_param = request.args.get("n")
    try:
        n = int(n_param) if n_param is not None else 1
    except ValueError:
        return _json({"error": "n must be an integer"}, 400)
    if n < 1 or n > 100:
        return _json({"error": "n must be between 1 and 100"}, 400)

    with get_conn(current_app.config["SETTINGS"]) as conn:
        if n == 1:
            raw_person = build_person(conn)
            return _json(format_person(raw_person))
        people = [format_person(build_person(conn)) for _ in range(n)]
        return _json(people)


@api_bp.get("/cpr")
def cpr_only():
    gender = random_gender()
    dob = random_birthdate()
    return _json({"CPR": make_cpr(dob, gender)})


@api_bp.get("/name-gender")
def name_gender():
    gender = random_gender()
    first, last = random_name(gender)
    return _json({"firstName": first, "lastName": last, "gender": gender})


@api_bp.get("/name-gender-dob")
def name_gender_dob():
    gender = random_gender()
    first, last = random_name(gender)
    dob = random_birthdate()
    return _json({"firstName": first, "lastName": last, "gender": gender, "birthDate": dob.isoformat()})


@api_bp.get("/cpr-name-gender")
def cpr_name_gender():
    gender = random_gender()
    dob = random_birthdate()
    first, last = random_name(gender)
    return _json({"CPR": make_cpr(dob, gender), "firstName": first, "lastName": last, "gender": gender})


@api_bp.get("/cpr-name-gender-dob")
def cpr_name_gender_dob():
    gender = random_gender()
    dob = random_birthdate()
    first, last = random_name(gender)
    return _json({
        "CPR": make_cpr(dob, gender),
        "firstName": first,
        "lastName": last,
        "gender": gender,
        "birthDate": dob.isoformat(),
    })


@api_bp.get("/address")
def address():
    with get_conn(current_app.config["SETTINGS"]) as conn:
        return _json(random_address(conn))


@api_bp.get("/phone")
def phone():
    return _json({"phoneNumber": random_phone()})
