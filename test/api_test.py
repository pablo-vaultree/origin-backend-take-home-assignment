import os
import tempfile

import pytest

from api.app import *


@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()

    yield client


@pytest.fixture
def analysis_data():
    analysis_data = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    yield analysis_data


def test_valid_request(client, analysis_data):

    response = client.post("/risk-profile", json=analysis_data)

    assert "economic" == response.get_json().get("auto")
    assert "economic" == response.get_json().get("home")
    assert "regular" == response.get_json().get("life")
    assert "ineligible" == response.get_json().get("disability")


def test_user_without_house_request(client, analysis_data):
    del analysis_data["house"]
    response = client.post("/risk-profile", json=analysis_data)

    assert "ineligible" == response.get_json().get("home")


def test_user_without_vehicle_request(client, analysis_data):
    del analysis_data["vehicle"]
    response = client.post("/risk-profile", json=analysis_data)

    assert "ineligible" == response.get_json().get("auto")


def test_invalid_request(client, analysis_data):

    analysis_data["age"] = "1"
    response = client.post("/risk-profile", json=analysis_data)

    assert response.status_code == 400
    assert "age" == response.get_json().get("field")
