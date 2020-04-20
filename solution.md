

POST /risk-profile

{
  "age": 35,
  "dependents": 2,
  "house": {"ownership_status": "owned"},
  "income": 0,
  "marital_status": "married",
  "risk_questions": [0, 1, 0],
  "vehicle": {"year": 2018}
}


{
    "auto": "regular",
    "disability": "ineligible",
    "home": "economic",
    "life": "regular"
}

- auto
- disability
- home
- life

InsurenceService
- Analysis (AnalysisData) : RiskProfile (auto, disability, home, life)

InsurencePofile
Evaluate(AnalysisData) : RiskProfile
CheckEligibility  : bool

AutoInsurencePofile : InsurencePofile

List<ScoreRuleStrategy> rules

Evaluate(AnalysisData) : RiskProfile
    CheckEligibility return ineligible

    CalculateScore 

    return EvaluateRiskProfileProfile

CalculateScore
    sum (rules)

EvaluateRiskProfileProfile

CheckEligibility  : bool
 hasCar


ScoreRuleStrategy : int

LessThan30Years 
Between30And40Years
Over60Years
LowIncome
HouseMortgaged
HasDependents
IsMarried
VehicleIsNew
