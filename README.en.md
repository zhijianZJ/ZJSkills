# Learning Architect

[简体中文](README.md)

**Version 1.0.0 · 84 tests · MIT**

Turn an ambiguous learning goal into a verifiable, adaptable, personalized learning system.

## What it helps you solve

Course lists rarely answer three critical questions: which capabilities the target actually requires, what evidence supports the current gap, and where to recompute when circumstances change. Learning Architect starts from the target, baseline, capacity, and constraints, then designs a competency model, project ladder, phased roadmap, weekly actions, and assessment gates while keeping facts, self-reports, evidence, inferences, and assumptions distinct.

It can improve the quality of learning decisions, capability evidence, and adaptation, but it does not guarantee an offer, career transition, promotion, income, or any result controlled by external parties.

## Quick start

Enable `learning-architect` in a Skill-capable AI tool, then state your target and constraints directly:

```text
Use Learning Architect to design my personalized learning system.
My target: build verifiable capabilities for an AI Agent Engineer role within six months.
My baseline: I can write basic Python scripts.
My weekly capacity: 12 hours.
My main constraint: limited budget, with a preference for project-first learning.
First ask for the decision-critical information that could change the route. Do not jump to course recommendations.
```

See [Getting Started](docs/getting-started.en.md) for prompts covering first use, continuation, and replanning.

## Install

Copy the repository's Skill directory into the Codex Skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./learning-architect "${CODEX_HOME:-$HOME/.codex}/skills/"
```

After installation, explicitly ask for `Learning Architect` in a new task. Other Skill-capable tools can import the same directory using their local Skill installation method.

## What you get

- A learner profile covering the target, baseline evidence, capacity, constraints, and risks.
- A competency tree and prerequisite dependencies derived backward from the target outcome.
- A project ladder centered on authentic artifacts and explicit rubrics.
- A phased roadmap, next weekly plan, and clear passing gates.
- Traceable structured state and versioned updates when the target, constraints, or evidence change.
- A reusable Domain Pack contract, with an AI Agent Engineer pack included in the repository.

## How it works

```text
Discovery → Goal Analysis → Gap Analysis → Competency Design → Curriculum Design
→ Project Design → Roadmap → Weekly Planner → Assessment → Outcome Preparation
→ Continuous Optimization
```

Each stage has entry conditions, artifacts, and a gate. When evidence is insufficient, the system labels assumptions or requests more information. When a project or assessment fails, it locates the earliest causal gap and recomputes only the affected downstream parts.

## Full documentation

- [Getting Started](docs/getting-started.en.md): first use, continuation, and replanning.
- [Full Usage Guide](docs/usage-guide.en.md): workflow, structured state, evidence judgment, and safety boundaries.
- [Scenarios and Prompts](docs/examples.en.md): complete examples for four typical targets.
- [Domain Pack Extension Guide](docs/domain-pack-guide.en.md): data contract, competency dependencies, project archetypes, and validation requirements.
- [中文文档](README.md): Chinese project entry.

## Project structure

| Location | Purpose |
| --- | --- |
| [`learning-architect/SKILL.md`](learning-architect/SKILL.md) | Core operating contract and workflow router |
| [`learning-architect/references/`](learning-architect/references/) | Discovery, competency, curriculum, project, assessment, and optimization engines |
| [`learning-architect/assets/`](learning-architect/assets/) | Schemas, templates, and Domain Packs |
| [`learning-architect/scripts/`](learning-architect/scripts/) | Offline learning-system validator |
| [`tests/learning-architect/`](tests/learning-architect/) | 84 regression tests plus valid and invalid fixtures |
| [`docs/`](docs/) | Chinese and English usage and extension guides |

## Contributing

Documentation fixes, reproducible issue reports, and new Domain Packs that follow the data contract are welcome. Read the [contribution guide](CONTRIBUTING.md) before submitting, and follow its evidence, privacy, brand-neutrality, and no-hidden-promotion boundaries.

## Initiator and maintainer

Initiated and maintained by ZJSkills.

## License

This project is available under the [MIT License](LICENSE).
