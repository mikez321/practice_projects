import unittest


class BetweenMarkersTest(unittest.TestCase):
    """Testing for between_markers function."""

    def test_it_returns_the_string_between_the_markers(self):
        """Given two markers it returns the string between them."""
        self.assertEqual(between_markers('What is >apple<', '>', '<'), 'apple')


if __name__ == '__main__':
    unittest.main()
