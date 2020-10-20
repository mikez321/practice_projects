"""Return a count of the frequency of dates."""
import unittest


def frequency(all_dates: list,
              match_day: str = 'x',
              match_month: str = 'x',
              match_year: str = 'x') -> int:
    """
    Return the frequency a day month or year occurrs in the given dates.

    :param all_dates: This is a list of all the possible dates to search
        through.
    :param match_day: A string representing the day of a month, default value
        is 'x' as a 'wildcard'.
    :param match_month: A string representing the number of a month, default
        value is 'x' as a 'wildcard'.
    :param match_year: A string representing the number of the year, default
        value is 'x' as a 'wildcard'.
    :return: The return is an integer representing the frequency of how often
        that day, month, or year occurrs in the provided dates.  It is possible
        to pass in more than one parameter at a time.

    :Examples:
        dates = ["3/21/2004", "3/19/2004", "3/21/2020"]
        frequency(dates, match_month='3')
        >>> 3
        frequency(dates, match_day='21')
        >>> 2
        frequency(dates, match_month='3', day='21')
        >>> 2
        frequency(dates, match_month='12')
        >>> 0
    """
    match_date = '/'.join([match_month, match_day, match_year])
    result = []

    for date in all_dates:
        if match_month == 'x':
            month = match_month
        else:
            month = date.split('/')[0]

        if match_day == 'x':
            day = match_day
        else:
            day = date.split('/')[1]

        if match_year == 'x':
            year = match_year
        else:
            year = date.split('/')[2]

        date = '/'.join([month, day, year])

        if match_date == date:
            result.append(date)

    return len(result)


class DateTest(unittest.TestCase):
    """Testing for dates."""

    def test_it_returns_frequency_by_month(self):
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

    def test_it_return_frequency_by_year(self):
        """Return a number representning the frequency of year input."""
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

        self.assertEqual(frequency(dates, match_year='2019'), 2)
        self.assertEqual(frequency(dates, match_year='2020'), 9)

    def test_it_return_frequency_by_day(self):
        """Return a number representning the frequency of year input."""
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

        self.assertEqual(frequency(dates, match_day='14'), 2)
        self.assertEqual(frequency(dates, match_day='11'), 3)

    def test_it_return_frequency_by_combinations_of_dates(self):
        """Return a number representning the frequency of year input."""
        dates = [
            "1/14/2019",
            "6/26/2019",
            "1/1/2020",
            "1/19/2020",
            "2/11/2020",
            "2/15/2020",
            "4/5/2020",
            "4/11/2020",
            "4/14/2020",
            "6/26/2020",
        ]

        self.assertEqual(frequency(dates, match_month='1', match_year='2020'), 2)
        self.assertEqual(frequency(dates, match_day='26', match_month='6'), 2)
        self.assertEqual(frequency(dates, match_month='2', match_year='2019'), 0)

if __name__ == '__main__':
    unittest.main()
