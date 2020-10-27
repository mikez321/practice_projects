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
    pass


def to_binary(num: int) -> int:
    """Convert a decimal int to a binary number."""
    binary = []

    while num != 0:
        binary.append(str(num % 2))
        num = num // 2

    return int(''.join(binary[::-1]))


class SortBitsTest(unittest.TestCase):
    """Testing for sortBits function."""

    @unittest.skip('Create binary conversion first')
    def test_it_sorts_numbers_based_on_their_binary_representation(self):
        """Sort ints in ascending order by number of 1s in their binary rep."""
        self.assertEqual(sort_bits([0, 1, 2, 3, 4, 5, 6, 7, 8]),
                         [0, 1, 2, 4, 8, 3, 5, 6, 7])

    def test_it_can_convert_a_number_to_binary(self):
        """It can convert a number to a binary number."""
        self.assertEqual(to_binary(2), 10)
        self.assertEqual(to_binary(3), 11)
        self.assertEqual(to_binary(15), 1111)
        self.assertEqual(to_binary(37), 100101)


if __name__ == '__main__':
    unittest.main()
