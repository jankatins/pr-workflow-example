import typing

import pytest

from calculator.__main__ import main


@pytest.mark.parametrize(
    "problem_input, result",
    (
        (["1 + 1"], 2),
        (["1", "+", "1"], 2),
    ),
)
def test_compute_happy_case(
    problem_input: typing.List[str],
    result: int,
    capsys: pytest.CaptureFixture,
) -> None:
    main(problem_input)
    captured = capsys.readouterr()
    calculation = " ".join(problem_input)
    assert captured.out == f"The result of '{calculation}' is: '{result}'\n"
    assert captured.err == ""


@pytest.mark.parametrize("problem_input, msg", ((["1+"], "Could not parse"),))
def test_compute_raises_on_unparseable_input(
    problem_input: typing.List[str],
    msg: str,
    capsys: pytest.CaptureFixture,
) -> None:
    main(problem_input)
    captured = capsys.readouterr()
    assert captured.out == "Could not parse '1+'\n"
    assert captured.err == ""
