incident = {
    "id": "INC-001",
    "description": (
        "An integration returns HTTP 401 "
        "after a credential change."
    ),
    "evidence": [],
}

print(f"Incident: {incident['id']}")
print(f"Description: {incident['description']}")
print(f"Evidence items: {len(incident['evidence'])}")



reference = {
    "category": "authentication",
    "root_cause_confirmed": False,
    "requires_more_evidence": True,
    "acceptable_next_checks": [
        "Inspect the authentication error details.",
        "Verify which credentials the integration is using.",
    ],
}


# Print the expected behaviour and next checks based on the reference data
print("\nExpected behaviour:")
print(f"Category: {reference['category']}")
print(f"Root cause confirmed: {reference['root_cause_confirmed']}")
print(f"More evidence needed: {reference['requires_more_evidence']}")

print("Acceptable next checks:")
for check in reference["acceptable_next_checks"]:
    print(f"- {check}")

def evaluate_response(response, reference):
    checks = {
        "category_correct": (
            response["category"] == reference["category"]
        ),
        "root_cause_status_correct": (
            response["root_cause_confirmed"]
            == reference["root_cause_confirmed"]
        ),
        "evidence_requirement_correct": (
            response["requires_more_evidence"]
            == reference["requires_more_evidence"]
        ),
    }

    return checks



def print_evaluation_results(title,evaluation_results):
    print(f"\n{title} evaluation results:")
    for name, passed in evaluation_results.items():
        status = "PASS" if passed else "FAIL"
        print(f"- {name}: {status}")


candidate_response = {
    "category": "authentication",
    "root_cause_confirmed": False,
    "requires_more_evidence": True,
}

results = evaluate_response(candidate_response, reference)


########## the overconfident response 

overconfident_response = {
    "category": "authentication",
    "root_cause_confirmed": True,
    "requires_more_evidence": False,
}

overconfident_results = evaluate_response(overconfident_response, reference)



############## end of overconfident response evaluation

######## PRINTING ############

print_evaluation_results("Standard candidate response", results)
print("\n #################################################")
print_evaluation_results("Overconfident response", overconfident_results)
