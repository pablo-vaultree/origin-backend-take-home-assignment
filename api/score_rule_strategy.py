from abc import ABC, abstractmethod
from models import *


class ScoreRuleStrategy(ABC):
    def calculate(analysis_data):
        pass


class LessThan30YearsRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysis_data):
        if analysis_data.age < 30:
            return self.__score

        return 0


class Between30And40YearsRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysis_data):
        if analysis_data.age >= 30 or analysis_data.age <= 40:
            return self.__score

        return 0


class LowIncomeRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysis_data):
        if analysis_data.income < 200000:
            return self.__score

        return 0


class HouseMortgagedRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysis_data):
        if analysis_data.house.ownership_status == OwnershipStatus.MORTGAGED:
            return self.__score

        return 0


class HasDependentsRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysis_data):
        if analysis_data.dependents > 0:
            return self.__score

        return 0


class IsMarriedRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysis_data):
        if analysis_data.marital_status == MaritalStatus.MARRIED:
            return self.__score

        return 0


class VehicleIsNewRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysis_data):
        if analysis_data.vehicle.years_old() <= 5:
            return self.__score

        return 0
