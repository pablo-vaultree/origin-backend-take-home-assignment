from dataclasses import dataclass
from enum import Enum
from typing import List
from abc import ABC, abstractmethod
from functools import reduce


class RiskProfileStatus(Enum):
    ECONOMIC = "economic"
    REGULAR = "regular"
    RESPONSIBLE = "responsible"
    INELIGIBLE = "ineligible"


class MaritalStatus(Enum):
    SINGLE = "single"
    MARRIED = "married"


class OwnershipStatus(Enum):
    OWNED = "owned"
    MORTGAGED = "mortgaged"


@dataclass
class HouseStatus:
    ownership_status: OwnershipStatus


@dataclass
class VehcleData:
    year: int


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
            disability=DisabilityInsurencePofile().evaluate(analysisData),
            home=HomeInsurencePofile().evaluate(analysisData),
            life=LifeInsurencePofile().evaluate(analysisData),
        )


class ScoreRuleStrategy(ABC):
    def calculate(analysisData):
        pass


class LessThan30YearsRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysisData):
        print(self.__score)
        if analysisData.age < 30:
            return self.__score

        return 0


class InsurencePofile(ABC):
    def evaluate(analysisData):
        pass

    def checkEligibility(analysisData):
        pass


class AutoInsurencePofile(InsurencePofile):
    def __init__(self):
        self.__rules = [LessThan30YearsRuleStrategy(5)]
        self.__score = 0

    def calculate_score(self, analysisData):
        for rule in self.__rules:
            self.__score += rule.calculate(analysisData)

    def checkEligibility(self, analysisData):
        return analysisData.vehicle is not None

    def evaluate(self, analysisData):
        if self.checkEligibility(analysisData) == False:
            return RiskProfileStatus.INELIGIBLE

        self.calculate_score(analysisData)

        if self.__score < 0:
            return RiskProfileStatus.ECONOMIC
        elif self.__score <= 1 or self.__score >= 2:
            return RiskProfileStatus.REGULAR
        else:
            return RiskProfileStatus.RESPONSIBLE


class HomeInsurencePofile(InsurencePofile):
    def evaluate(self, analysisData):
        if self.checkEligibility(analysisData) == False:
            return RiskProfileStatus.INELIGIBLE

        return RiskProfileStatus.ECONOMIC

    def checkEligibility(self, analysisData):
        return analysisData.house.ownership_status == OwnershipStatus.OWNED


class LifeInsurencePofile(InsurencePofile):
    def evaluate(self, analysisData):
        if self.checkEligibility(analysisData) == False:
            return RiskProfileStatus.INELIGIBLE

        return RiskProfileStatus.REGULAR

    def checkEligibility(self, analysisData):
        is_under_60_years = analysisData.age <= 60
        return analysisData.age <= 60


class DisabilityInsurencePofile(InsurencePofile):
    def evaluate(self, analysisData):
        if self.checkEligibility(analysisData) == False:
            return RiskProfileStatus.INELIGIBLE

        return RiskProfileStatus.REGULAR

    def checkEligibility(self, analysisData):
        has_income = analysisData.income > 0
        is_under_60_years = analysisData.age <= 60
        return has_income and is_under_60_years
