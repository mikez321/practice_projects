"""Days between challenge from checkio."""


def days_diff(date1: tuple, date2: tuple) -> int:
    """
    Return the days between two dates.

    :param date1: A date passed in as a tuple of ints in the format of
        (year, month, day).
    :param date2: This is another tuple of ints in the same format as date1.
    :return:  The difference in number of days between the two dates is
        returned.  It will always be a positive value or zero.
    """
    months = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    y1, m1, d1 = date1
    elapsed_days = 0
    for year in range(1, y1 + 1):
        if year % 4 == 0:
            elapsed_days += 1

    for month in months.keys():
        if m1 > month:
            elapsed_days += months[month]
    days1 = y1 * 365 + elapsed_days + d1

    y2, m2, d2 = date2
    elapsed_days = 0
    for year in range(1, y2 + 1):
        if year % 4 == 0:
            elapsed_days += 1
    for month in months.keys():
        if m2 > month:
            elapsed_days += months[month]
    days2 = y2 * 365 + elapsed_days + d2

    return abs(days1 - days2)
