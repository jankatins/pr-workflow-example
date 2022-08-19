# PR Workflow Example

This repo allows someone to practise PRs like they would happen with open source projects. It assumes someone knows
basic git but wants to learn how to interact with an open source repo.

## Features

- Multiple changes possible: python code, python tests, markdown docs
- CI/CD pipeline (via Github actions) which runs linters and tests for python and linters for markdown files
    - Some errors get annotations: black, isort, and flake8 violations for python and any spelling errors
- Aims at [scaled trunk based development workflow](https://trunkbaseddevelopment.com/) with a main branch and
  short-lived feature branches

## Instruction

1. Fork the repo
2. Clone the repo from your personal fork
3. Create a new branch
4. Do changes in the code/text. See the README.md for [Python code](calculator/README.md) and [docs](docs/README.md)
    - Coordinate with others to create merge conflicts by changing the same lines in the code in different ways
5. Commit and push to your fork
6. Create PR
7. Add additional changes by either additional commits or changing commits/rebases and force pushes
    - Fix CI/CD failures
    - Fix merge conflicts
8. Wait for the maintainer to get it merged

## Used github actions

- Spell checking via [check-spelling action](https://github.com/marketplace/actions/check-spelling)
- Markdownlint-cli via [markdownlint-cli action](https://github.com/marketplace/actions/markdownlint-cli)
- flake8 via [TrueBrain/actions-flake8](https://github.com/marketplace/actions/flake8-with-annotations)
- Mypy: [jpetrucciani/mypy-check](https://github.com/marketplace/actions/mypy-check)
- pytest
- black with annotations via diff
  by [reviewdog/action-suggester](https://github.com/marketplace/actions/reviewdog-suggester-suggest-any-code-changes-based-on-diff-with-reviewdog)
- isort with annotations via diff
  by [reviewdog/action-suggester](https://github.com/marketplace/actions/reviewdog-suggester-suggest-any-code-changes-based-on-diff-with-reviewdog)
