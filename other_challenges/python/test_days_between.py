"""Testing for days between challenge."""
from days_between import days_diff


def test_it_can_return_a_few_days_apart():
    """Return the difference in two close together days."""
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3


def test_it_can_return_a_larger_date_range():
    """Return the difference in two far apart days."""
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238


def test_it_can_return_days_over_many_years():
    """Return he difference in two days years apart."""
    assert days_diff((2014, 1, 1), (2012, 1, 1)) == 730
