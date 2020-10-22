"""Between markers lite challenge from py.checkio.org."""
import unittest


def between_markers(input: str, mk1: str, mk2: str) -> str:
    """
    Return the string inside the markers.

    :param input: Any string which shoudl include markers.
    :param mk1: This is the first marker and should be included in 'input.'
    :param mk2: This is the 2nd marker and should also be included in 'input.'
    :return: The return is whatever is encased in the markers.
    """
    return input[input.index(mk1) + 1:input.index(mk2)]


class BetweenMarkersTest(unittest.TestCase):
    """Testing for between_markers function."""

    def test_it_returns_the_string_between_the_markers(self):
        """Given two markers it returns the string between them."""
        self.assertEqual(between_markers('What is >apple<', '>', '<'), 'apple')


if __name__ == '__main__':
    unittest.main()
