"""SortBits Cassidoo Challenge."""
import unittest


def sort_bits(nums: list) -> list:
    """
    Sort the integers by the number of 1’s in their binary representation.

    :param nums: A list of ints.
    :return: A sorted list of the ints in nums, sorted in assending order by
        the number of 1s in their binary representation.
    :example:
        sort_bits([0,1,2,3,4,5,6,7,8])
        >>> [0,1,2,4,8,3,5,6,7]
    """


class SortBitsTest(unittest.TestCase):
    """Testing for sortBits function."""

    def test_it_sorts_numbers_based_on_their_binary_representation(self):
        """Sort ints in ascending order by number of 1s in their binary rep."""
        self.assertEqual(sort_bits([0, 1, 2, 3, 4, 5, 6, 7, 8]),
                         [0, 1, 2, 4, 8, 3, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()
