"""Come up with a solution in O(n) or less."""
import unittest

# Given an array that was once sorted in ascending order is rotated at some
# pivot unknown to you beforehand (so [0,2,4,7,9] might become [7,9,0,2,4],
# for example). Find the minimum value in that array in O(n) or less.


def min_num(nums):
    """
    Return the lowest number in the shifted list.

    :param nums: A list of numbers that were in ascending order, but have been
        rotated at some point.  (Example: [0, 2, 4, 7, 9] might become
        [7, 9, 0, 2, 4])
    """
    return None


class MinNumTest(unittest.TestCase):
    """Return the min value in the list."""

    def test_it_returns_the_lowest_value(self):
        """Return the lowest value in O(n)."""
        test = [7, 9, 0, 2, 4]
        self.assertEqual(min_num(test), 0)


if __name__ == '__main__':
    unittest.main()
