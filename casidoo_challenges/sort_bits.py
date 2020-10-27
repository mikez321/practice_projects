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
    for num in order_list(nums):
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


def place(num: int, num_list: list) -> list:
    """
    Place a number in a list in ascending order.

    :param num: The given int that needs to be placed in a list.
    :param num_list: A list of ints (this can be an empty list).
    :return: The given num_list will be returned with the new num added in
        ascending order.
    """
    if len(num_list) == 0:
        num_list.append(num)
        return num_list
    elif num > num_list[-1]:
        num_list.append(num)
        return num_list
    elif num < num_list[0]:
        return [num] + num_list
    else:
        for i, n in enumerate(num_list):
            if n < num:
                continue
            else:
                place_index = i

            return num_list[:place_index] + [num] + num_list[place_index:]


def order_list(num_list: list) -> list:
    """
    Return a list of ints in ascending order.

    :param num_list: A list of ints in any order.
    :return: The original list of numbers in ascending order.
    """
    ordered_list = []
    for num in num_list:
        ordered_list = place(num, ordered_list)

    return ordered_list


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

    def test_it_can_place_a_number_in_ascending_order_in_a_list(self):
        """Given a number and a list it can place that number in order."""
        self.assertEqual(place(3, []), [3])
        self.assertEqual(place(9, [3]), [3, 9])
        self.assertEqual(place(1, [3, 9]), [1, 3, 9])
        self.assertEqual(place(7, [1, 3, 9]), [1, 3, 7, 9])

    def test_it_can_sort_a_list_of_ints(self):
        """It can arrange a list of ints in ascending order."""
        self.assertEqual(order_list([3, 9, 21, 1, 0]), [0, 1, 3, 9, 21])


if __name__ == '__main__':
    unittest.main()
