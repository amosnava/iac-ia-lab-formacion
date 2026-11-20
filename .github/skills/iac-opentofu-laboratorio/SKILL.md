---
name: iac-opentofu-laboratorio
description: Use when continuing or completing an exercise in this repository's fictional OpenTofu lab, especially changes spanning variables, local modules, plans, policy, GitHub Actions, and traceability.
---

# Laboratorio IaC con OpenTofu

Use this skill to extend the existing personal lab safely from one exercise to the next. Treat the course guide as the requirement, but inspect the real repository before editing.

## Safety and starting point

- Read the exercise guide and inspect the current branch, worktree status, `origin`, relevant files, and latest successful Actions run.
- Do not edit until the baseline is understood. Start from the previous exercise branch or another base explicitly requested by the user. Use the user's branch name when it differs from the guide.
- Preserve unrelated local changes and commits. Never reset, discard, force-push, or include unrelated work in the exercise branch.
- Work only in the user's personal repository, not the course template or instructor repository.
- Do not add cloud providers or credentials. Never run `tofu apply` or `tofu destroy`.

## Data flow and policy changes

- Trace each scenario value through the full path: root variable or `.tfvars` value → root module argument → module input variable → `terraform_data`'s `input` → plan JSON → policy.
- Keep fictional labels in `terraform_data.input`; do not describe them as native cloud tags.
- Preserve prior policy checks while adding new ones. Validate exact resource addresses, types, actions, required keys, known/sensitive values, allowed environments, and any environment-to-owner mapping.
- Inspect nested `after_unknown` and `after_sensitive` structures recursively. Boolean `false` means not marked; any nested boolean `true` means marked. Do not reject a non-empty map just because it exists.
- Check that an environment is allowed before looking up its expected owner, so invalid input cannot cause a missing-key failure.

## Validate and demonstrate behavior

- Prefer the repository's existing GitHub Actions workflow for OpenTofu plans and policy execution. Do not install OpenTofu or Python just for this lab when Actions can validate the commit.
- Predict the correct and incorrect scenario outcomes before the controlled test. Change only the intended test value. A wrong but well-typed owner should pass formatting, validation, and plan, then fail at the relevant policy step.
- Restore the approved value and verify the corrected Actions run is actually green before claiming success. A skipped step is not a passing check.
- Keep the workflow unchanged unless the exercise explicitly requires it. Confirm the plan workflow does not apply or destroy resources.

## Traceability and delivery

- Create the requested exercise trace folder and record the starting commit/branch, decisions, changed files, predictions, commits, pushes, Action run URLs and outcomes, correction, and PR/merge status.
- Update the README with the purpose, rule, controlled failure, correction, and lab limitations when requested.
- Review the final diff and `git diff --check`; confirm temporary invalid values are absent from the final configuration.
- Commit and push only to the exercise branch when authorized. If a PR is requested, target the user's repository and the specified base branch; never merge unless explicitly authorized.
- After PR creation or merge, update the trace with the actual status and verify any resulting Actions run.
