import os
import tempfile

import pytest

from api.app import *


@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()

    yield client


def test_valid_request(client):
    user = {
        "age": 35,
        "dependents": 2,
        "house": {"ownership_status": "owned"},
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 0],
        "vehicle": {"year": 2018},
    }

    response = client.post("/risk-profile", json=user)

    assert "economic" == response.get_json().get("auto")
    assert "economic" == response.get_json().get("home")
    assert "regular" == response.get_json().get("life")
    assert "ineligible" == response.get_json().get("disability")
