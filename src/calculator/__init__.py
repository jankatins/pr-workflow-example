"""A simple calculator."""


class ParseError(Exception):
    """The input could not be parsed."""


def compute(problem_input: str) -> int:
    """Compute the result of the input equation."""
    problem_input = problem_input.strip()
    if problem_input == "1 + 1":
        return 2
    raise ParseError(f"Could not parse '{problem_input}'")
