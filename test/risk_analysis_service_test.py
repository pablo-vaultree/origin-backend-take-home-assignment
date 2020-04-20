import pytest

from api.risk_analysis_service import *

analysis_data = AnalysisData(
    age=28,
    dependents=2,
    house=HouseStatus(OwnershipStatus.OWNED),
    income=0,
    marital_status=MaritalStatus.MARRIED,
    risk_questions=[0, 1, 0],
    vehicle=VehcleData(year=2018),
)


def test_default_should_return_risk_profile_plan():
    profile = InsurenceService.analysis(analysis_data)

    assert profile.auto == RiskProfileStatus.REGULAR
    assert profile.disability == RiskProfileStatus.INELIGIBLE
    assert profile.home == RiskProfileStatus.ECONOMIC
    assert profile.life == RiskProfileStatus.REGULAR
