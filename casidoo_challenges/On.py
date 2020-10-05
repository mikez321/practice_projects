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

    Of note: This function uses enumerate() which returns an index as it is
        on that item in the loop.  Enumerate will operate on On (linear) time
        and looking up items in a list by index (nums[index] and
        nums[index +1]) will operate on O1 (constant).  Therefore the time
        complexity of this function is On.
    """
    for index, num in enumerate(nums):
        if nums[index] > nums[index + 1]:
            return nums[index + 1]
            break


class MinNumTest(unittest.TestCase):
    """Return the min value in the list."""

    def test_it_returns_the_lowest_value(self):
        """Return the lowest value in O(n)."""
        test = [7, 9, 0, 2, 4]
        self.assertEqual(min_num(test), 0)


if __name__ == '__main__':
    unittest.main()
