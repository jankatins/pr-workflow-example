# Example python app: a simple calculator

A stupid calculator which currently can only calculate '1 + 1'.

Call the example app via

```shell
python -m calculator 1 + 1
```

## Instruction

The current example app can compute the result of '1 + 1', but nothing more. Try to make it more useful or at least more
robust (e.g. '1+1' already fails...).

## Dev Setup

There is a makefile which sets up the virtual env, if you want it. Call `make run` to let makefile set-up the venv
in `venv` and call the example app.

The tests are in the `tests` subdirectory and can be called via `pytest`. `make test` will install the right packages
into the venv. Linters (black, isort, flake8, mypy) als also callable and can be triggered by `make lint`.

To add more packages to the venv, add them in `requirements.txt.in` and run `make update-packages` It will regenerate
the venv and the pinned versions in `requirement.txt`. Please check in both files together with the code changes.
