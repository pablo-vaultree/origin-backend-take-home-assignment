from models import *
from insurence_profile import *


class InsurenceService:
    def analysis(self, analysis_data):
        return RiskProfilePlan(
            auto=AutoInsurencePofile().evaluate(analysis_data),
            disability=DisabilityInsurencePofile().evaluate(analysis_data),
            home=HomeInsurencePofile().evaluate(analysis_data),
            life=LifeInsurencePofile().evaluate(analysis_data),
        )
