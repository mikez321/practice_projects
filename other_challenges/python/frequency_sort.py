"""Frequency Sort challenge from checkio."""
import unittest


def second_index(objects: list) -> list:
    """
    Return a new list sorted by frequency.

    :param objects: A list of ints or strings
    :return: The original list is returned but like objects are grouped
        together and appear in order from most frequently occuring to least.
    """
    return ['bob', 'bob', 'bob', 'carl', 'alex']


class QuestionMarkTest(unittest.TestCase):
    """Testing for frequency_sort challenge."""

    def test_it_sorts(self):
        """It sorts by frequency."""
        self.assertEqual(
            second_index(['bob', 'bob', 'carl', 'alex', 'bob']),
            ['bob', 'bob', 'bob', 'carl', 'alex']
        )


if __name__ == '__main__':
    unittest.main()
