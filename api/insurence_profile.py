from abc import ABC, abstractmethod
from models import *
from score_rule_strategy import *


class InsurencePofile(ABC):
    def calculate_score(self, analysis_data):
        score = analysis_data.base_score()
        for rule in self.rules:
            score += rule.calculate(analysis_data)

        return score

    def evaluate(self, analysis_data):
        pass

    def check_eligibility(self, analysis_data):
        pass

    def calculate_profile(self, score):
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

    def check_eligibility(self, analysis_data):
        return analysis_data.vehicle is not None

    def evaluate(self, analysis_data):
        if self.check_eligibility(analysis_data) == False:
            return RiskProfileStatus.INELIGIBLE

        score = self.calculate_score(analysis_data)

        return self.calculate_profile(score)


class HomeInsurencePofile(InsurencePofile):
    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            LowIncomeRuleStrategy(-1),
            HouseMortgagedRuleStrategy(1),
        ]

    def evaluate(self, analysis_data):
        if self.check_eligibility(analysis_data) == False:
            return RiskProfileStatus.INELIGIBLE

        score = self.calculate_score(analysis_data)
        return self.calculate_profile(score)

    def check_eligibility(self, analysis_data):
        return analysis_data.house is not None


class LifeInsurencePofile(InsurencePofile):
    def __init__(self):
        self.rules = [
            LessThan30YearsRuleStrategy(-2),
            Between30And40YearsRuleStrategy(-1),
            LowIncomeRuleStrategy(-1),
            HasDependentsRuleStrategy(1),
            IsMarriedRuleStrategy(1),
        ]

    def evaluate(self, analysis_data):
        if self.check_eligibility(analysis_data) == False:
            return RiskProfileStatus.INELIGIBLE

        score = self.calculate_score(analysis_data)

        return self.calculate_profile(score)

    def check_eligibility(self, analysis_data):
        is_under_60_years = analysis_data.age <= 60
        return analysis_data.age <= 60


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

    def evaluate(self, analysis_data):
        if self.check_eligibility(analysis_data) == False:
            return RiskProfileStatus.INELIGIBLE

        score = self.calculate_score(analysis_data)

        return self.calculate_profile(score)

    def check_eligibility(self, analysis_data):
        has_income = analysis_data.income > 0
        is_under_60_years = analysis_data.age <= 60
        return has_income and is_under_60_years
