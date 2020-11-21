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


class SplitListTest(unittest.TestCase):
    """Testing for split_list function."""

    def test_it_splits_a_list(self):
        """It can split a single list into two lists."""
        self.assertEqual(
            split_list([1, 2, 3, 4, 5, 6]), [[1, 2, 3], [4, 5, 6]]
        )


if __name__ == '__main__':
    unittest.main()
