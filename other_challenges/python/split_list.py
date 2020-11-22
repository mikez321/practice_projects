"""Split list challenge from checkio."""
import unittest


def split_list(items: list) -> list:
    """
    Return two lists from a single list.

    :param items: This is a list and can contain an even or odd number of
        items.
    :return: If the number of items in the list is even, the function will
        return a list of two lits of equal numbers of items from the first.
        If the original list has an odd number of items, the first list will
        contain one more item than the second.
    """
    if len(items) == 1:
        return [items, []]
    else:
        split = (len(items) // 2) * -1
        first_half = items[:split]
        second_half = items[len(items) - 1:split - 1:-1]

        return [first_half, second_half[::-1]]


class SplitListTest(unittest.TestCase):
    """Testing for split_list function."""

    def test_it_can_split_nothing(self):
        """If an empty list is provided an empty list is returned."""
        self.assertEqual(split_list([]), [[], []])

    def test_it_can_split_a_list_of_one_item(self):
        """It can split a single item in a list."""
        assert split_list([1]) == [[1], []]

    def test_it_splits_a_list(self):
        """It can split a single list into two lists."""
        self.assertEqual(
            split_list([1, 2, 3, 4, 5, 6]), [[1, 2, 3], [4, 5, 6]]
        )


if __name__ == '__main__':
    unittest.main()
