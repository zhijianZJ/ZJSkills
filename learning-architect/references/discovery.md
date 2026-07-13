# Progressive Discovery

Discover only information that can change the next learning-system decision. Use `assets/question-banks/discovery.yaml`; do not administer it as a fixed questionnaire.

## Question routing

1. Identify the pending decision and its competing routes.
2. List unknowns that could change the selected route, its feasibility, sequence, evidence standard, or learner safety.
3. Rank candidate questions by expected information gain: `decision_change_probability * decision_impact * uncertainty_reduction`, discounted by response burden and sensitivity.
4. Ask the smallest coherent batch, normally one to three questions.
5. Skip questions already answered by current, credible evidence. Ask sensitive questions only with consent and always permit “prefer not to answer.”
6. Stop when remaining answers would not materially change the current decision. Record them in `unknowns` rather than inventing precision.

If the learner refuses discovery, request only target outcome, present baseline, deadline, and weekly capacity when they are decision-critical. When safe, provide a provisional `draft` whose assumptions, `source`, `confidence`, and validation needs are explicit.

## Evidence-labeled learner profile

Populate the learner-profile contract: `personal`, `experience`, `learning_preferences`, `motivation`, `constraints`, `swot`, and `unknowns`. For every material item include or link:

- `value`: the claim used by the system;
- `source`: user, assessment, project, mentor, employer, market-research, or inference;
- `confidence`: a numeric value from 0 to 1;
- `evidence_ids`: supporting artifacts when available;
- `decision_impact`: what changes if the claim is wrong.

Never convert self-report into verified competence. Resolve contradictions with a small task or evidence request, not by choosing the more convenient statement.

## SWOT output

Generate an evidence-labeled SWOT with four explicit keys:

- `Strength`: internal assets already supported by evidence or clearly marked self-report.
- `Weakness`: internal gaps or habits that impede the target; describe behavior, never moral character.
- `Opportunity`: external or contextual openings the learner can realistically use.
- `Risk`: internal or external conditions that threaten feasibility, safety, persistence, or evidence quality.

Attach `source`, `confidence`, and a decision implication to every SWOT item. End with decision-critical unknowns and the next highest-information question or validation task.
