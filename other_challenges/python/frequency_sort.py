"""Frequency Sort challenge from checkio."""
import unittest


def num_in_list(li):
    """Return the length of a list."""
    return len(li)


def frequency_sort(items: list) -> list:
    """
    Return a new list sorted by frequency.

    :param items: A list of ints or strings
    :return: The original list is returned but like items are grouped
        together and appear in order from most frequently occuring to least.
    """
    ind_lists = {}
    gathered_lists = []
    result = []

    for item in items:
        if ind_lists.get(item) is not None:
            ind_lists[item].append(item)
        else:
            ind_lists[item] = [item]

    for group in ind_lists:
        gathered_lists.append(ind_lists[group])

    gathered_lists.sort(reverse=True, key=num_in_list)

    for group in gathered_lists:
        for item in group:
            result.append(item)

    return result


class QuestionMarkTest(unittest.TestCase):
    """Testing for frequency_sort challenge."""

    def test_it_sorts(self):
        """It sorts by frequency."""
        self.assertEqual(
            frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']),
            ['bob', 'bob', 'bob', 'carl', 'alex']
        )
        self.assertEqual(
            frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]),
            [4, 4, 4, 4, 6, 6, 2, 2]
        )


if __name__ == '__main__':
    unittest.main()
