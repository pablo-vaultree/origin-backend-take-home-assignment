from dataclasses import dataclass
from enum import Enum
from typing import List


class RiskProfileStatus(Enum):
    "economic"
    "regular"
    "responsible"
    "ineligible"


@dataclass
class HouseStatus:
    ownership_status: str


@dataclass
class VehcleData:
    year: int


@dataclass
class MaritalStatus(Enum):
    "single"
    "married"


@dataclass
class AnalysisData:
    age: int
    dependents: int
    house: HouseStatus
    income: int
    marital_status: MaritalStatus
    risk_questions: List[int]
    vehicle: VehcleData


@dataclass
class RiskProfilePlan:
    auto: RiskProfileStatus
    disability: RiskProfileStatus
    home: RiskProfileStatus
    life: RiskProfileStatus


class InsurenceService:
    def analysis(analysisData):
        return RiskProfilePlan(
            auto="regular", disability="regular", home="regular", life="regular"
        )
