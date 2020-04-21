#!flask/bin/python
from flask import Flask, request, jsonify, make_response
from functools import wraps
from dacite import from_dict
from dacite import Config
from risk_analysis_service import *
from models import *
import logging

app = Flask(__name__)


def validate_fields(f):
    wraps(f)

    def validate(*args, **kwargs):
        return f(*args, **kwargs)

    return validate


@app.route("/risk-profile", methods=["POST"])
@validate_fields
def riskProfile():
    analysis_data = from_dict(
        data_class=AnalysisData, data=request.get_json(), config=Config(cast=[Enum])
    )

    profile = InsurenceService().analysis(analysis_data)

    return make_response(jsonify(profile), 200)


if __name__ == "__main__":
    app.run(debug=True)
