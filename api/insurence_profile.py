from abc import ABC, abstractmethod
from models import *
from score_rule_strategy import *


class InsurencePofile(ABC):
    def calculateScore(self, analysisData):
        score = analysisData.baseScore()
        for rule in self.rules:
            score += rule.calculate(analysisData)

        return score

    def evaluate(self, analysisData):
        pass

    def checkEligibility(self, analysisData):
        pass

    def calculateProfile(self, score):
        print(str(self) + str(score))
        if score <= 0:
            return RiskProfileStatus.ECONOMIC
        elif score <= 2:
            return RiskProfileStatus.REGULAR
        else:
            return RiskProfileStatus.RESPONSIBLE


class AutoInsurencePofile(InsurencePofile):
    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            VehicleIsNewRuleStrategy(1),
            LowIncomeRuleStrategy(-1),
        ]

    def checkEligibility(self, analysisData):
        return analysisData.vehicle is not None

    def evaluate(self, analysisData):
        if self.checkEligibility(analysisData) == False:
            return RiskProfileStatus.INELIGIBLE

        score = self.calculateScore(analysisData)

        return self.calculateProfile(score)


class HomeInsurencePofile(InsurencePofile):
    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            LowIncomeRuleStrategy(-1),
            HouseMortgagedRuleStrategy(1),
        ]

    def evaluate(self, analysisData):
        if self.checkEligibility(analysisData) == False:
            return RiskProfileStatus.INELIGIBLE

        score = self.calculateScore(analysisData)
        return self.calculateProfile(score)

    def checkEligibility(self, analysisData):
        return analysisData.house is not None


class LifeInsurencePofile(InsurencePofile):
    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            LowIncomeRuleStrategy(-1),
            HasDependentsRuleStrategy(1),
            IsMarriedRuleStrategy(1),
        ]

    def evaluate(self, analysisData):
        if self.checkEligibility(analysisData) == False:
            return RiskProfileStatus.INELIGIBLE

        score = self.calculateScore(analysisData)

        return self.calculateProfile(score)

    def checkEligibility(self, analysisData):
        is_under_60_years = analysisData.age <= 60
        return analysisData.age <= 60


class DisabilityInsurencePofile(InsurencePofile):
    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            LowIncomeRuleStrategy(-1),
            HouseMortgagedRuleStrategy(1),
            HasDependentsRuleStrategy(1),
            IsMarriedRuleStrategy(-1),
        ]

    def evaluate(self, analysisData):
        if self.checkEligibility(analysisData) == False:
            return RiskProfileStatus.INELIGIBLE

        score = self.calculateScore(analysisData)

        return self.calculateProfile(score)

    def checkEligibility(self, analysisData):
        has_income = analysisData.income > 0
        is_under_60_years = analysisData.age <= 60
        return has_income and is_under_60_years
