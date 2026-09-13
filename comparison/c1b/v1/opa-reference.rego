package ehco_c1b.reference

default result := {"disposition": "WITHHOLD", "permitted": false, "reason": "REQUIRED_CONDITION_NOT_SATISFIED"}

supported_action if {
  input.action_class == "SYNTHETIC_PREINTELLIGENCE_GATE"
}

required_conditions_satisfied if {
  input.conditions.identity_condition == "SATISFIED"
  input.conditions.permission_condition == "SATISFIED"
  input.conditions.eligibility_condition == "SATISFIED"
  input.conditions.source_condition == "SATISFIED"
  input.conditions.range_condition == "SATISFIED"
  input.conditions.evidence_condition == "SATISFIED"
}

result := {"disposition": "UNSUPPORTED_REQUEST", "permitted": false, "reason": "UNSUPPORTED_ACTION"} if {
  not supported_action
}

result := {"disposition": "RETAIN_AMBIGUITY", "permitted": false, "reason": "AMBIGUOUS_REQUIRED_STATE"} if {
  supported_action
  input.conditions.ambiguity_condition == "AMBIGUOUS"
}

result := {"disposition": "PASS", "permitted": true, "reason": "ALL_FROZEN_CONDITIONS_SATISFIED"} if {
  supported_action
  input.conditions.ambiguity_condition == "CLEAR"
  required_conditions_satisfied
}
