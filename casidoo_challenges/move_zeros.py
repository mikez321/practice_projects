"""Move zeros to the end of the list."""
import unittest
# Given an array of random integers, move all the zeros in the array to the end
# of the array. Try to keep this in O(n) time (or better)!
# Example:
# moveZeros([1, 2, 0, 1, 0, 0, 3, 6])
# [1, 2, 1, 3, 6, 0, 0, 0]


def move_zeros(numbers_list: list, zeros: list = []) -> list:
    """
    Rearrange the list and move zeros to the end.

    :param numbers_list: A given list of numbers (positive or negative)
    :return: The original list of numbers, but with any zeros moved the end
        of the list.
    """
    for index in range(len(numbers_list) - 1, -1, -1):
        if numbers_list[index] == 0:
            zeros.append(0)
            del numbers_list[index]
    return numbers_list + zeros


class MoveZerosTest(unittest.TestCase):
    """It will move zeros to the end of the list."""

    def test_move_zeros_to_the_end_of_the_list(self):
        """Zeros will be moved to the end of the list."""
        given = [1, 2, 0, 1, 0, 0, 3, 6]
        expected = [1, 2, 1, 3, 6, 0, 0, 0]
        self.assertEqual(move_zeros(given), expected)


if __name__ == '__main__':
    unittest.main()
