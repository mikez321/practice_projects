"""Remove unique elements from a list."""
import unittest


def non_uniques(elems: list) -> list:
    """
    Return the non-unique elements in a given list.

    :param elems: A list of elements.
    :return: The elements in the original list are returned but if they are
        unique, they will be eliminated from the returned list.
    """
    item_index = range(len(elems))[::-1]

    for index in item_index:
        if elems.count(elems[index]) == 1:
            del(elems[index])

    return elems


class NonUniqueTest(unittest.TestCase):
    """Testing for non unique elements function."""

    def test_it_returns_only_non_unique_elements(self):
        """Return a list of the non-unique elements of a given list."""
        self.assertEqual(non_uniques([1, 2, 3, 1, 3]), [1, 3, 1, 3])


if __name__ == '__main__':
    unittest.main()
