# Incident Investigation Agent

A learning and portfolio project exploring reliable AI-assisted
incident investigation using Python, structured evaluations,
and eventually LangGraph.

## Current implementation

The project currently contains:

- A fictional integration incident.
- A manually defined reference describing expected behaviour.
- A manually defined candidate response.
- A Python evaluator comparing three structured fields:
  - Incident category.
  - Whether the root cause is confirmed.
  - Whether more evidence is required.

No language model is connected yet.

## Why evaluation comes first

An assistant should distinguish observed facts from hypotheses.

For example, an HTTP 401 response after a credential change
suggests an authentication-related issue, but does not establish
the exact root cause.

The evaluator checks whether a candidate response agrees with
the reference expectations. A FAIL result indicates a mismatch;
it does not necessarily mean the program malfunctioned.

## Run locally

Requires Python 3. No external packages are currently required.

From the project directory:

    python3 main.py

The script prints the incident, reference expectations,
and PASS/FAIL results.

## Planned development

- Add multiple fictional incidents.
- Evaluate model-generated structured responses.
- Retrieve relevant fictional runbooks.
- Implement an investigation workflow with LangGraph.
- Compare versions through regression evaluations.
- Explore LLM-as-judge evaluation.

## Limitations

The current evaluator checks three field values.
It does not assess free-text reasoning, evidence support,
or the quality of recommended actions.

This is an educational prototype, not a production system.

## Data

Examples are fictional. Do not contribute confidential
company data, credentials, or internal runbooks.