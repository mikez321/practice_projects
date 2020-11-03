"""Testing for days between challenge."""
from days_between import days_diff


def test_it_can_return_a_few_days_apart():
    """Return the difference in two close together days."""
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
