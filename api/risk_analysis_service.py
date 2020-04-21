from models import *
from insurence_profile import *


class InsurenceService:
    def analysis(self, analysisData):
        return RiskProfilePlan(
            auto=AutoInsurencePofile().evaluate(analysisData),
            disability=DisabilityInsurencePofile().evaluate(analysisData),
            home=HomeInsurencePofile().evaluate(analysisData),
            life=LifeInsurencePofile().evaluate(analysisData),
        )
