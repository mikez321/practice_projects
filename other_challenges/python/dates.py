"""Return a count of the frequency of dates."""
import unittest


def frequency(all_dates: list,
              match_day: str = None,
              match_month: str = None,
              match_year: str = None) -> int:
    """
    Return the frequency a day month or year occurrs in the given dates.

    :param all_dates: This is a list of all the possible dates to search
        through.
    :param day: A string representing the day of a month
    :param month: A string representing the number of a month
    :param year: A string representing the number of the year
    :return: The return is an integer representing the frequency of how often
        that day, month, or year occurrs in the provided dates.  It is possible
        to pass in more than one parameter at a time.

    :Examples:
        dates = ["3/21/2004", "3/19/2004", "3/21/2020"]
        frequency(dates, month='3')
        >>> 3
        frequency(dates, day='21')
        >>> 2
        frequency(dates, month='3', day='21')
        >>> 2
        frequency(dates, month='12')
        >>> 0
    """
    matches = []
    for date in all_dates:
        month = date.split('/')[0]
        day = date.split('/')[1]
        year = date.split('/')[2]

        if month == match_month:
            matches.append(date)

    return len(matches)


class DateTest(unittest.TestCase):
    """Testing for dates."""

    def test_it_returns_a_frequency_of_dates(self):
        """Return a number representning the frequency of date input."""
        dates = [
            "11/14/2019",
            "12/26/2019",
            "1/1/2020",
            "1/19/2020",
            "2/11/2020",
            "2/15/2020",
            "3/11/2020",
            "4/5/2020",
            "4/11/2020",
            "4/14/2020",
            "4/26/2020",
        ]

        self.assertEqual(frequency(dates, match_month='3'), 1)
        self.assertEqual(frequency(dates, match_month='1'), 2)
        self.assertEqual(frequency(dates, match_month='4'), 4)


if __name__ == '__main__':
    unittest.main()
