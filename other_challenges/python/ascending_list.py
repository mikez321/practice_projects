"""Ascending list challenge from checkio."""
import unittest


def is_ascending(nums: list) -> bool:
    """
    Return true if all elements in a list are in least to greatest order.
    :param nums: A list of ints
    :return: If the list is sorted from least to greatest value the function
        should return True.  Otherwise, it will return False.
    """
    if len(nums) == 0 or len(nums) == 1:
        return True


class IsAscendingTest(unittest.TestCase):
    """Testing for is_ascending function."""

    def test_no_numbers_is_true(self):
        """No numbers in the list is True."""
        self.assertEqual(is_ascending([]), True)

    def test_single_number(self):
        """A single number returns True."""
        self.assertEqual(is_ascending([99]), True)

    def test_it_can_do_two_nums(self):
        """Return True if the first number is greater than the second."""
        self.assertEqual(is_ascending([1, 10]), True)
        self.assertEqual(is_ascending([10, 1]), False)

    def test_equal_is_not_ascending(self):
        """Two equal numbers are not considered ascending."""
        self.assertEqual(is_ascending([1, 1]), False)

    def test_it_can_do_multiple_nums(self):
        """It works on larger lists."""
        self.assertEqual(is_ascending([-5, 10, 99, 123456]), True)
        self.assertEqual(is_ascending([4, 5, 6, 7, 3, 7, 9]), False)


if __name__ == '__main__':
    unittest.main()
