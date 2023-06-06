"""Basic tests for the calculator."""
import pytest
from calculator import ParseError, compute


@pytest.mark.parametrize(
    ("problem_input", "result"),
    [
        ("1 + 1", 2),
        # The next two do not work yet
        # ("1+1", 2), # Found commented out code
        # ("2-1", 1), # Found commented out code
    ],
)
def test_compute_happy_case(problem_input: str, result: int) -> None:
    """Test the happy case."""
    assert compute(problem_input) == result


@pytest.mark.parametrize(("problem_input", "msg"), [("1+", "Could not parse")])
def test_compute_raises_on_unparseable_input(problem_input: str, msg: str) -> None:
    """Test that bad code raises and exception."""
    with pytest.raises(ParseError, match=msg):
        compute(problem_input)
