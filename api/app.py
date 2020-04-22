from flask import Flask, request, jsonify, make_response
from functools import wraps
from dacite import from_dict
from dacite import Config
from risk_analysis_service import *
from typing import List
from models import *
import logging

app = Flask(__name__)


def validate_fields(f):
    wraps(f)

    def validate(*args, **kwargs):
        data = request.get_json()

        error = {}
        error["message"] = "Field is invalid"

        if "age" not in data or type(data["age"]) is not int:
            error["field"] = "age"
            return make_response(jsonify(error), 400)

        if "dependents" not in data or type(data["age"]) is not int:
            error["field"] = "dependents"
            return make_response(jsonify(error), 400)

        if "income" not in data or type(data["age"]) is not int:
            error["field"] = "income"
            return make_response(jsonify(error), 400)

        if "marital_status" not in data:
            error["field"] = "marital_status"
            return make_response(jsonify(error), 400)

        if "risk_questions" not in data or len(data["risk_questions"]) != 3:
            error["field"] = "risk_questions"
            return make_response(jsonify(error), 400)

        return f(*args, **kwargs)

    return validate


@app.route("/risk-profile", methods=["POST"])
@validate_fields
def risk_profile():
    analysis_data = from_dict(
        data_class=AnalysisData, data=request.get_json(), config=Config(cast=[Enum])
    )

    profile = InsurenceService().analysis(analysis_data)

    return make_response(jsonify(profile), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
