# PR Workflow Example

This repo allows someone to practice PRs like they would happen with open source projects. It assumes someone knows
basic git but wants to learn how to interact with an open source repo.

See [README_code.md](README_code.md) for the regular readme.

## Features

- Multiple changes possible: python code, python tests, markdown docs
- CI/CD pipeline (via Github actions) which runs linters and tests for python and linters for markdown files
    - Some errors get annotations: black, isort, and flake8 violations for python and any spelling errors
- Aims at [scaled trunk based development workflow](https://trunkbaseddevelopment.com/) with a main branch and
  short-lived feature branches
- [MIT licensed](LICENCE)

## Instruction

1. Fork the repo
2. Clone the repo from your personal fork (using ssh!)
3. Add upstream to your local repo to enable pulling the latest changes from
   it: `git remote add upstream https://github.com/jankatins/pr-workflow-example.git`
4. Create a new branch: `git checkout -b 'new_feature'`
5. Initialize the virtualenv: `poetry install` and run the code: `poetry run python -m calculator '1 + 1'`
6. Do changes in the code/text. See the README.md for [Python code](calculator/README.md) and [docs](docs/README.md)
    - Coordinate with others to create merge conflicts by changing the same lines in the code in different ways
    - Add a [changelog](https://keepachangelog.com/en/1.0.0/)
7. Check your code: first add your changes to the git index `git add -u -p` and then
   run `poetry run pre-commit run --all-files` (fix and repeat until all is fine)
8. Commit `git commit -m "Add new feature"` and push to your fork: `git push origin`
9. Create the PR in the github web ui: <https://github.com/jankatins/pr-workflow-example>
10. Add additional changes by either additional commits or changing commits/rebases and force pushes
    - Fix CI/CD failures
    - Fix merge conflicts
11. Wait for the maintainer to get it merged

## Details

- [Poetry](https://python-poetry.org/) as python package manager
- [mkdocs](https://www.mkdocs.org/) for documentation + automatic upload of the docs on releases to a github
  page ([example](https://jankatins.github.io/pr-workflow-example/))
- [pytest](https://docs.pytest.org/) python unit testing + PR annotations via
  [utgwkk/pytest-github-actions-annotate-failures](https://github.com/utgwkk/pytest-github-actions-annotate-failures)
- [Black](https://black.readthedocs.io/en/stable/) and [isort](https://github.com/PyCQA/isort) python code formatter
- [flake8](https://flake8.pycqa.org/en/latest/) and [mypy](http://www.mypy-lang.org/) python code checking
- [cspell](https://cspell.org/) spell checking including inline annotations
- [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) markdown linting
- [pre-commit](https://pre-commit.com/) for all checks above + some additional ones
- [Changelog](CHANGELOG.md) for relevant code changes based
  on ["keep a changelog"](https://keepachangelog.com/en/1.0.0/)
- [Pull request template](.github/pull_request_template.md) for PR checklists
- Automatic PRs for [dependency updates](.github/workflows/dependencies.yml)
  and [updates from the cookiecutter template](.github/workflows/cookiecutter.yml)

---

This project was generated using
the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.
