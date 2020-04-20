from dataclasses import dataclass
from enum import Enum
from typing import List
from abc import ABC, abstractmethod


class RiskProfileStatus(Enum):
    ECONOMIC = "economic"
    REGULAR = "regular"
    RESPONSIBLE = "responsible"
    INELIGIBLE = "ineligible"


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
            auto=AutoInsurencePofile().evaluate(analysisData),
            disability=DisabilityInsurencePofile.evaluate(analysisData),
            home=HomeInsurencePofile.evaluate(analysisData),
            life=LifeInsurencePofile.evaluate(analysisData),
        )


class InsurencePofile(ABC):
    def evaluate(analysisData):
        pass

    def checkEligibility(analysisData):
        pass


class AutoInsurencePofile(InsurencePofile):
    def checkEligibility(self, analysisData):
        return analysisData.vehicle is not None

    def evaluate(self, analysisData):
        if self.checkEligibility(analysisData) == False:
            return RiskProfileStatus.INELIGIBLE

        return RiskProfileStatus.REGULAR


class HomeInsurencePofile(InsurencePofile):
    def evaluate(analysisData):
        return RiskProfileStatus.ECONOMIC

    def checkEligibility(analysisData):
        return analysisData.home != null


class LifeInsurencePofile(InsurencePofile):
    def evaluate(analysisData):
        return RiskProfileStatus.REGULAR

    def checkEligibility(analysisData):
        has_income = analysisData.income != null and income.income > 0
        is_under_60_years = analysisData.age <= 60
        return has_income and is_under_60_years


class DisabilityInsurencePofile(InsurencePofile):
    def evaluate(analysisData):
        return RiskProfileStatus.INELIGIBLE

    def checkEligibility(analysisData):
        has_income = analysisData.income != null and income.income > 0
        is_under_60_years = analysisData.age <= 60
        return has_income and is_under_60_years
