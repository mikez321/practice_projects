"""Find the nearest value."""
import unittest


def nearest_value(nums: set, target: int) -> int:
    """
    Return the number in the set that is closest to the target.

    :param nums: A set of integers sorted in ascending order.
    :param target: The number to be evaluated.
    :return: The return value is the number in the set closest to the target.
        If there are two numbers in the set equally close, the smaller of the
        two numbers is returned.
    """
    result = None
    smallest_distance = None
    for num in nums:
        distance = abs(target - num)

        if result is None:
            result = num
            smallest_distance = distance
        else:
            if distance < smallest_distance:
                smallest_distance = distance
                result = num

    return result


class NearestTest(unittest.TestCase):
    """Testing for nearest value."""

    def test_it_finds_the_nearest_number_in_the_list(self):
        """It will find the nearest value in the list to the given number."""
        self.assertEqual(nearest_value({4, 7, 10, 11, 12, 17}, 9), 10)

    def test_if_two_nums_are_equal_distance_the_smaller_wins(self):
        """Price is right rules here."""
        self.assertEqual(nearest_value({4, 7, 9, 10, 11, 12, 17}, 8), 7)


if __name__ == '__main__':
    unittest.main()
