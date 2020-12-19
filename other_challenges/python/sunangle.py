"""Sun angle challenge from checkio."""
import unittest


def sun_angle(time: str) -> float:
    """Calculate the angle of the sun at a given time."""
    return 0


def time_as_minutes(time: str) -> int:
    """Given a time as a string calculate how many minutes are in that time."""
    hours = int(time.split(':')[0]) * 60
    minutes = int(time.split(':')[1])

    return hours + minutes


class SunAngleTest(unittest.TestCase):
    """Testing for angle of sun at a given time."""

    def test_it_returns_total_minutes_in_a_day(self):
        """Given a string of time, it will return time as minutes."""
        self.assertEqual(time_as_minutes("0:24"), 24)
        self.assertEqual(time_as_minutes("1:30"), 90)
        self.assertEqual(time_as_minutes("6:00"), 360)
        self.assertEqual(time_as_minutes("18:30"), 1110)

    def test_zero_degrees_at_sunrise(self):
        self.assertEqual(sun_angle("06:00"), 0)

    def test_zero_degrees_at_sunset(self):
        self.assertEqual(sun_angle("18:00"), 0)

    def test_90_degrees_at_noon(self):
        self.assertEqual(sun_angle("12:00"), 90)

if __name__ == '__main__':
    unittest.main()
