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
    num_collection = {}
    result = []
    nums.sort()
    for num in nums:
        if to_binary(num).count('1') in num_collection.keys():
            num_collection[to_binary(num).count('1')].append(num)
        else:
            num_collection[to_binary(num).count('1')] = [num]

    for group in num_collection.values():
        for num in group:
            result.append(num)

    return result


def to_binary(num: int) -> int:
    """Convert a decimal int to a binary number."""
    binary = []

    if num == 0:
        return '0'

    while num != 0:
        binary.append(str(num % 2))
        num = num // 2

    return ''.join(binary[::-1])


class SortBitsTest(unittest.TestCase):
    """Testing for sortBits function."""

    def test_it_sorts_numbers_based_on_their_binary_representation(self):
        """Sort ints in ascending order by number of 1s in their binary rep."""
        self.assertEqual(sort_bits([0, 1, 2, 3, 4, 5, 6, 7, 8]),
                         [0, 1, 2, 4, 8, 3, 5, 6, 7])

    def test_numbers_can_be_in_any_order(self):
        """The sorting doesn't need to be in any order."""
        self.assertEqual(sort_bits([8, 0, 1, 3, 5, 4, 2, 6, 7]),
                         [0, 1, 2, 4, 8, 3, 5, 6, 7])

    def test_it_can_convert_a_number_to_binary(self):
        """It can convert a number to a binary number."""
        self.assertEqual(to_binary(2), '10')
        self.assertEqual(to_binary(3), '11')
        self.assertEqual(to_binary(15), '1111')
        self.assertEqual(to_binary(37), '100101')


if __name__ == '__main__':
    unittest.main()
