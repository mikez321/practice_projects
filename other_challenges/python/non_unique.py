"""Remove unique elements from a list."""
import unittest


class NonUniqueTest(unittest.TestCase):
    """Testing for non unique elements function."""

    def test_it_returns_only_non_unique_elements(self):
        """Return a list of the non-unique elements of a given list."""
        # self.assertEqual(non_uniques([1, 2, 3, 1, 3]), [1, 3, 1, 3])
        pass


if __name__ == '__main__':
    unittest.main()
