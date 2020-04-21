from dataclasses import dataclass
from enum import Enum
from typing import List
from flask_inputs import Inputs
from wtforms.validators import DataRequired, NumberRange
import datetime


class RiskProfileStatus(str, Enum):
    ECONOMIC: str = "economic"
    REGULAR: str = "regular"
    RESPONSIBLE: str = "responsible"
    INELIGIBLE: str = "ineligible"


class MaritalStatus(str, Enum):
    SINGLE: str = "single"
    MARRIED: str = "married"


class OwnershipStatus(str, Enum):
    OWNED: str = "owned"
    MORTGAGED: str = "mortgaged"


@dataclass
class HouseStatus:
    ownership_status: OwnershipStatus


@dataclass
class VehcleData:
    year: int

    def yearsOld(self):
        return datetime.date.today().year - self.year


class AnalysisDataValidate(Inputs):
    rule = {
        "age": [NumberRange(min=0)],
        "dependents": [NumberRange(min=0)],
        "house": [NumberRange(min=0)],
    }


@dataclass
class AnalysisData:
    age: int
    dependents: int
    house: HouseStatus
    income: int
    marital_status: MaritalStatus
    risk_questions: List[int]
    vehicle: VehcleData

    def baseScore(self):
        return sum(self.risk_questions)


@dataclass
class RiskProfilePlan:
    auto: RiskProfileStatus
    disability: RiskProfileStatus
    home: RiskProfileStatus
    life: RiskProfileStatus
