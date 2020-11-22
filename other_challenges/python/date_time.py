"""DateTime challenge from checkio."""
import unittest


def format_day(day: str) -> str:
    """Remove prepended zeros from a day."""
    return(str(int(day)))


def format_month(month: str) -> str:
    """Return the name of the month that matches its number."""
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',
    }
    return months[int(month)]


def format_year(year: str) -> str:
    """Remove prepended zeros from year and add word 'year'."""
    return str(int(year)) + ' year'


def format_hour(hour: str) -> str:
    """Return a properly formatted version of the hours given as a string."""
    hour = int(hour)
    if hour == 1:
        return str(hour) + ' hour'
    else:
        return str(hour) + ' hours'


def format_minute(minute: str) -> str:
    """Return a properly formatted version of the minutes given as a string."""
    minute = int(minute)
    if minute == 1:
        return str(minute) + ' minute'
    else:
        return str(minute) + ' minutes'


def date_time(date_time: str) -> str:
    """
    Convert number time to human readable time.

    :param date_time: A string of numbers representing a date and time in the
        format DD.MM.YYYY HH:MM  (ex: '01.01.2000 12:30' representing
        1 January 2000, 12:30 PM)  *Time will be 24 hour format.
    :return: A human readable version of the date and time will be returned in
        the format of '1 January 2000 year 1 hour 59 minutes'  *Note that time
        will be referred to as 'hour' and 'minute' for a single hour or single
        minute, but 'hours' and 'minutes' for times like
        '2 hours and 25 minutes.'
    """
    date = date_time.split()[0]
    time = date_time.split()[-1]
    formatted_date = [
        format_day(date.split('.')[0]),
        format_month(date.split('.')[1]),
        format_year(date.split('.')[2]),
        format_hour(time.split(':')[0]),
        format_minute(time.split(':')[1]),
    ]

    return " ".join(formatted_date)


class DateTimeTest(unittest.TestCase):
    """Testing for date_time function."""

    def test_it_can_return_a_day_with_or_without_zeros(self):
        """Days with leading zeros will be returned as just the number."""
        self.assertEqual(format_day('01'), '1')
        self.assertEqual(format_day('31'), '31')

    def test_it_returns_the_name_of_a_month(self):
        """Given a number, it will return that month."""
        self.assertEqual(format_month('01'), 'January')
        self.assertEqual(format_month('11'), 'November')

    def test_it_properly_formats_a_year(self):
        """Years prepended with zeros will be retuned without the zeros."""
        self.assertEqual(format_year('2000'), '2000 year')
        self.assertEqual(format_year('1998'), '1998 year')
        self.assertEqual(format_year('0041'), '41 year')

    def test_it_properly_formats_hours(self):
        """Return hour without leading zeros and proper version of 'hour'."""
        self.assertEqual(format_hour('00'), '0 hours')
        self.assertEqual(format_hour('01'), '1 hour')
        self.assertEqual(format_hour('11'), '11 hours')

    def test_it_properly_formats_minutes(self):
        """Return mins without leading zeros and proper version of 'hour'."""
        self.assertEqual(format_minute('00'), '0 minutes')
        self.assertEqual(format_minute('01'), '1 minute')
        self.assertEqual(format_minute('11'), '11 minutes')

    def test_it_can_return_a_human_readable_date(self):
        """Given date as numbers, it can spell it out in normal format."""
        self.assertEqual(
            date_time("01.01.2000 00:00"),
            "1 January 2000 year 0 hours 0 minutes"
        )

        self.assertEqual(
            date_time("19.09.2999 01:59"),
            "19 September 2999 year 1 hour 59 minutes"
        )

        self.assertEqual(
            date_time("21.10.1999 18:01"),
            "21 October 1999 year 18 hours 1 minute"
        )


if __name__ == '__main__':
    unittest.main()
