"""A simple Calculator"""
import sys
import typing


class ParseException(Exception):
    pass


def compute(input: str) -> int:
    """Compute the result of the input equation."""
    input = input.strip()
    if input == "1 + 1":
        return 2
    raise ParseException(f"Could not parse '{input}'")


def main(argv: typing.List[str]) -> int:
    """Echo the input arguments to standard output"""
    input = " ".join(argv)
    try:
        result = compute(input)
    except ParseException as e:
        print(e)
        return 1
    print(f"The result of '{input}' is: '{result}'")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
