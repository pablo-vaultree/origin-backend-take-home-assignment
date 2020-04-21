from abc import ABC, abstractmethod
from models import *


class ScoreRuleStrategy(ABC):
    def calculate(analysisData):
        pass


class LessThan30YearsRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysisData):
        if analysisData.age < 30:
            return self.__score

        return 0


class Between30And40YearsRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysisData):
        if analysisData.age >= 30 or analysisData.age <= 40:
            return self.__score

        return 0


class LowIncomeRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysisData):
        if analysisData.income < 200000:
            return self.__score

        return 0


class HouseMortgagedRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysisData):
        if analysisData.house.ownership_status == OwnershipStatus.MORTGAGED:
            return self.__score

        return 0


class HasDependentsRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysisData):
        if analysisData.dependents > 0:
            return self.__score

        return 0


class IsMarriedRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysisData):
        if analysisData.marital_status == MaritalStatus.MARRIED:
            return self.__score

        return 0


class VehicleIsNewRuleStrategy(ScoreRuleStrategy):
    def __init__(self, score):
        self.__score = score

    def calculate(self, analysisData):
        if analysisData.vehicle.yearsOld() <= 5:
            return self.__score

        return 0
