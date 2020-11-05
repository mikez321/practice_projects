"""Days between challenge from checkio."""
from datetime import datetime


def days_diff(date1: tuple, date2: tuple) -> int:
    """
    Return the days between two dates.

    :param date1: A date passed in as a tuple of ints in the format of
        (year, month, day).
    :param date2: This is another tuple of ints in the same format as date1.
    :return:  The difference in number of days between the two dates is
        returned.  It will always be a positive value or zero.
    """
    y1, m1, d1 = date1
    y2, m2, d2 = date2
    delta = datetime(y1, m1, d1) - datetime(y2, m2, d2)
    return(abs(delta.days))
