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


def test_it_can_take_leap_years_into_account():
    """Every 4 years is a leap year."""
    assert days_diff((1, 1, 1), (2, 1, 1,)) == 365
    assert days_diff((3, 1, 1), (4, 1, 1,)) == 366
#
# def test_it_can_return_days_from_the_start_to_the_end_of_time():
#     """Start from 1 and end at 9999."""
#     assert days_diff((1, 1, 1), (9999, 12, 31)) == 3652058
