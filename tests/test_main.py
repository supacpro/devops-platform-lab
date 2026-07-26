from app.main import add, is_even


def test_add_returns_sum() -> None:
    assert add(2, 3) == 5


def test_is_even_true_for_even_numbers() -> None:
    assert is_even(4)


def test_is_even_false_for_odd_numbers() -> None:
    assert not is_even(3)
