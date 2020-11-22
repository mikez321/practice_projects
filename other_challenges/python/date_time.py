"""DateTime challenge from checkio."""
import unittest


def date_time(date: str) -> str:
    """
    Convert number time to human readable time.

    :param date: A string of numbers representing a date and time in the format
        DD.MM.YYYY HH:MM  (ex: '01.01.2000 12:30' representing
        1 January 2000, 12:30 PM)  *Time will be 24hour format.
    :return: A human readable version of the date and time will be returned in
        the format of '1 January 2000 year 1 hour 59 minutes'  *Note that time
        will be referred to as 'hour' and 'minute' for a single hour or single
        minute, but 'hours' and 'minutes' for times like
        '2 hours and 25 minutes.'
    """


class DateTimeTest(unittest.TestCase):
    """Testing for date_time function."""

    def test_it_can_return_a_human_readable_date(self):
        """Given date as numbers, it can spell it out in normal format."""
        self.assertEqual(
            date_time("01.01.2000 00:00"),
            "1 January 2000 year 0 hours 0 minutes"
        )


if __name__ == '__main__':
    unittest.main()
