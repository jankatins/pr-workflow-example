import pytest

from calculator.__main__ import ParseException, compute


@pytest.mark.parametrize(
    "input, result",
    (
        ("1 + 1", 2),
        # The next two do not work yet
        # ("1+1", 2),
        # ("2-1", 1),
    ),
)
def test_compute_happy_case(input: str, result: int):
    assert compute(input) == result


@pytest.mark.parametrize("input, msg", (("1+", "Could not parse"),))
def test_compute_raises_on_unparseable_input(input: str, msg: str):
    with pytest.raises(ParseException, match=msg):
        compute(input)
