import pytest

from api.risk_analysis_service import *
from api.models import *

analysis_data = AnalysisData(
    age=35,
    dependents=2,
    house=HouseStatus(OwnershipStatus.OWNED),
    income=0,
    marital_status=MaritalStatus.MARRIED,
    risk_questions=[0, 1, 0],
    vehicle=VehcleData(year=2018),
)


def test_default_should_return_risk_profile_plan():
    profile = InsurenceService().analysis(analysis_data)

    assert profile.auto == RiskProfileStatus.ECONOMIC
    assert profile.disability == RiskProfileStatus.INELIGIBLE
    assert profile.home == RiskProfileStatus.ECONOMIC
    assert profile.life == RiskProfileStatus.REGULAR


def test_user_without_car_should_be_inelible_for_auto():
    analysis_data.vehicle = None
    profile = InsurenceService().analysis(analysis_data)

    assert profile.auto == RiskProfileStatus.INELIGIBLE


def test_user_without_house_should_be_inelible_for_home():
    analysis_data.house = None
    profile = InsurenceService().analysis(analysis_data)

    assert profile.home == RiskProfileStatus.INELIGIBLE


def test_user_without_income_should_be_inelible_for_disability():
    analysis_data.income = 0
    profile = InsurenceService().analysis(analysis_data)

    assert profile.disability == RiskProfileStatus.INELIGIBLE
