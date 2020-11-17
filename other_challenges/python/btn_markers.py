"""Between markers lite challenge from py.checkio.org."""
import unittest


def between_markers(input: str, mk1: str, mk2: str) -> str:
    """
    Return the string inside the markers.

    :param input: Any string which should include markers.
    :param mk1: This is the first marker and should be included in 'input.'
    :param mk2: This is the 2nd marker and should also be included in 'input.'
    :return: The return is whatever is encased in the markers.
    """
    if mk1 in input and mk2 in input:
        return input[input.index(mk1) + len(mk1):input.index(mk2)]
    elif mk1 in input:
        return input[input.index(mk1) + len(mk1):]
    elif mk2 in input:
        return input[:input.index(mk2)]
    else:
        return input


class BetweenMarkersTest(unittest.TestCase):
    """Testing for between_markers function."""

    def test_it_returns_the_string_between_the_markers(self):
        """Given two markers it returns the string between them."""
        self.assertEqual(between_markers('What is >apple<', '>', '<'), 'apple')

    def test_markers_can_be_longer_than_one_symbol(self):
        """Markers can be longer than one symbol."""
        self.assertEqual(between_markers(
            "<head><title>My new site</title></head>", "<title>", "</title>"),
                'My new site')


if __name__ == '__main__':
    unittest.main()
