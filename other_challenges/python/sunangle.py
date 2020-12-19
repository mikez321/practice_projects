"""Sun angle challenge from checkio."""
import unittest


def sun_angle(time: str) -> float:
    """Calculate the angle of the sun at a given time."""
    elapsed_mins = time_as_minutes(time)
    if 360 <= elapsed_mins <= 1080:
        # 1440 mins in a day, 360 deg in a circle, offset by 90deg
        # compare the fraction of minutes per day to degrees in a circle
        # and then offset by 90 degrees so 6 is 0 deg and 18 is 180 deg
        return elapsed_mins / 1440 * 360 - 90
    else:
        return "I don't see the sun"


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
        """Sun angle is 0 at sunrise."""
        self.assertEqual(sun_angle("06:00"), 0)

    def test_zero_degrees_at_sunset(self):
        """Sun angle is 180 at sunset."""
        self.assertEqual(sun_angle("18:00"), 180)

    def test_no_sun_before_6_or_after_6(self):
        """The sun is not in the sky before 6am or after 6pm."""
        self.assertEqual(sun_angle("0:24"), "I don't see the sun")
        self.assertEqual(sun_angle("1:30"), "I don't see the sun")
        self.assertEqual(sun_angle("18:30"), "I don't see the sun")

    def test_90_degrees_at_noon(self):
        """Sun is at 90 degrees at noon."""
        self.assertEqual(sun_angle("12:00"), 90)

    def test_it_can_calculate_other_angles(self):
        """Variable angles can be calculated too."""
        self.assertEqual(sun_angle("12:15"), 93.75)


if __name__ == '__main__':
    unittest.main()
