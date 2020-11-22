"""DateTime challenge from checkio."""
import unittest


def date_time(date_time: str) -> str:
    """
    Convert number time to human readable time.

    :param date_time: A string of numbers representing a date and time in the
        format DD.MM.YYYY HH:MM  (ex: '01.01.2000 12:30' representing
        1 January 2000, 12:30 PM)  *Time will be 24hour format.
    :return: A human readable version of the date and time will be returned in
        the format of '1 January 2000 year 1 hour 59 minutes'  *Note that time
        will be referred to as 'hour' and 'minute' for a single hour or single
        minute, but 'hours' and 'minutes' for times like
        '2 hours and 25 minutes.'
    """
    months = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }

    date = date_time.split()[0]
    day = date.split('.')[0]
    month = months[date.split('.')[1]]
    year = date.split('.')[-1]

    if day[0] == '0':
        day = day[1:]

    time = date_time.split()[-1]
    minutes = time.split(':')[-1]
    hours = time.split(':')[0]

    if minutes[0] == '0':
        minutes = minutes[1:]

    if hours[0] == '0':
        hours = hours[1:]

    if minutes == '1':
        minutes = minutes + ' minute'
    else:
        minutes = minutes + ' minutes'

    if hours == '1':
        hours = hours + ' hour'
    else:
        hours = hours + ' hours'

    return day + ' ' + month + ' ' + year + ' year ' + hours + ' ' + minutes


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
