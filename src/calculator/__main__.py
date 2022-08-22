"""A simple Calculator"""
import sys
import typing

from . import ParseException, compute


def main(argv: typing.List[str]) -> int:
    """Echo the input arguments to standard output"""
    problem_input = " ".join(argv)
    try:
        result = compute(problem_input)
    except ParseException as e:
        print(e)
        return 1
    print(f"The result of '{problem_input}' is: '{result}'")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv[1:]))  # pragma: no cover
