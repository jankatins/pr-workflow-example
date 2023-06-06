"""A simple Calculator."""
import sys

from . import ParseError, compute


def main(argv: list[str]) -> int:
    """Echo the input arguments to standard output."""
    problem_input = " ".join(argv)
    try:
        result = compute(problem_input)
    except ParseError as e:
        print(e)  # noqa: T201 `print` found
        return 1
    print(f"The result of '{problem_input}' is: '{result}'")  # noqa: T201 `print` found
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv[1:]))  # pragma: no cover
