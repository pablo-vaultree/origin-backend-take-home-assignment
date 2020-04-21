import pytest

from api.risk_analysis_service import *
from api.models import *

@pytest.fixture
def analysis_data():
    return AnalysisData(
        age=35,
        dependents=2,
        house=HouseStatus(OwnershipStatus.OWNED),
        income=0,
        marital_status=MaritalStatus.MARRIED,
        risk_questions=[0, 1, 0],
        vehicle=VehcleData(year=2018),
    )


def test_default_should_return_risk_profile_plan(analysis_data):
    profile = InsurenceService().analysis(analysis_data)    
    assert profile.auto == RiskProfileStatus.ECONOMIC
    assert profile.disability == RiskProfileStatus.INELIGIBLE
    assert profile.home == RiskProfileStatus.ECONOMIC
    assert profile.life == RiskProfileStatus.REGULAR


def test_user_without_car_should_be_ineligible_for_auto(analysis_data):
    analysis_data.vehicle = None
    profile = InsurenceService().analysis(analysis_data)

    assert profile.auto == RiskProfileStatus.INELIGIBLE


def test_user_without_house_should_be_ineligible_for_home(analysis_data):
    analysis_data.house = None
    profile = InsurenceService().analysis(analysis_data)

    assert profile.home == RiskProfileStatus.INELIGIBLE


def test_user_without_income_should_be_ineligible_for_disability(analysis_data):
    analysis_data.income = 0
    profile = InsurenceService().analysis(analysis_data)

    assert profile.disability == RiskProfileStatus.INELIGIBLE


def test_user_over_60_year_should_be_ineligible_for_disability_and_life(analysis_data):
    analysis_data.age = 61
    profile = InsurenceService().analysis(analysis_data)

    assert profile.disability == RiskProfileStatus.INELIGIBLE
    assert profile.life == RiskProfileStatus.INELIGIBLE


def test_user_house_is_mortgaged(analysis_data):
    analysis_data.house = HouseStatus(OwnershipStatus.MORTGAGED)
    profile = InsurenceService().analysis(analysis_data)

    assert profile.home == RiskProfileStatus.ECONOMIC
