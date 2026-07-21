# Changelog

All notable public changes to ZJSkills are recorded here.

## [3.1.0] - 2026-07-21

### Changed

- Career diagnosis now translates demonstrated experience into transferable career assets, testable opportunity hypotheses, and explicit unverified boundaries.
- A returned minimum-experience result now closes with one of four stage decisions: route-ready, compare further, build foundations first, or apply in the current role first.
- Current salary, hiring-window, and other market claims now require a named source, publication date, applicable region, and sample or method limitations; structural guidance remains available when that evidence is missing.

## [3.0.1] - 2026-07-20

### Changed

- Made learning-support recommendations diagnosis-first instead of defaulting to anti-enrollment language.
- Treated courses, memberships, mentors, communities, and institutions as valid options when they solve a named feedback, correction, practice, accountability, or structure need.
- Refocused Chinese and English user documentation on personal diagnosis, problem decomposition, learning routes, and getting unstuck.

### Removed

- Removed the standalone self-study-versus-training discussion and course-selection framing from learner-facing guides and examples.

## [3.0.0] - 2026-07-20

### Changed

- Intentionally replaced the full Education OS runtime with a lightweight, AI-first career diagnosis Skill.
- Reduced public use to three context-aware modes: career diagnosis, a learning route of at most three stages, and one-step learning help.
- Made chat the default output; one Markdown route is saved only on explicit request.
- Kept the technical name `zjskills`, explicit calls `$zjskills` and `/zjskills`, repository URL, five platform categories, and MIT license.

### Removed

- Removed the old schema, template, script, state-machine, and packaged-domain runtime architecture.
- Removed obsolete public extension guides. Git history remains the archive for removed implementation details.

### Migration

- Back up and replace the installed Skill directory rather than merging releases in place.
- Keep every user-created learning file. An old YAML workspace may be supplied as source material and summarized into one readable Markdown route.
