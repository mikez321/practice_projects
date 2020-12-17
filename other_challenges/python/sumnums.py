"""Sum Nums challenge from Niklas."""
import unittest


def sumnums(nums: list) -> list:
    """
    Return a new list containing the sums of all numbers to an index as values.

    :param nums: A list of ints
    :return: A new list of ints.  Each number returned in the new list will be
        the sum of all numbers leading up to it.
    :example:
        sumnums([1, 2, 3, 4])
        >>> [1, 3, 6, 10]
        sumnums([1, 1, 1, 1, 1, 1])
        >>> [1, 2, 3, 4, 5, 6]
        sumnums([1, 3, 1, 8])
        >>> [1, 4, 5, 13]
    """


class SplitListTest(unittest.TestCase):
    """Testing for sumnums function."""

    def test_it_returns_summed_nums(self):
        self.assertEqual(sumnums([1, 2, 3, 4]), [1, 3, 6, 10])



if __name__ == '__main__':
    unittest.main()
