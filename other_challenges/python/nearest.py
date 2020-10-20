"""Find the nearest value."""
import unittest


class NearestTest(unittest.TestCase):
    """Testing for nearest value."""

    def test_it_finds_the_nearest_number_in_the_list(self):
        """It will find the nearest value in the list to the given number."""
        self.assertEqual(nearest_value({4, 7, 10, 11, 12, 17}, 9), 10)

    @unittest.skip('One test at a time please.')
    def test_if_two_nums_are_equal_distance_the_smaller_wins(self):
        """Price is right rules here."""
        self.assertEqual(nearest_value({4, 7, 9, 10, 11, 12, 17}, 8), 7)


if __name__ == '__main__':
    unittest.main()
