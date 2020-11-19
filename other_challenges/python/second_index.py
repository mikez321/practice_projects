"""Second index challenge from checkio."""
import unittest


def second_index(text: str, char: str) -> int:
    """
    Return the index of the second instance of a given character.

    :param text: Any string of text, numbers, characters.
    :char: The 'target' character.  The function will give the index of the
        second occurance of this character.
    :return: The index position of the second instance of the char will be
        returned.  If there is not a second instance of this character the
        function will return None.
    """
    pass


class QuestionMarkTest(unittest.TestCase):
    """Testing for Second Index challenge."""

    def test_it_returns_the_second_index_of_the_char(self):
        """It will return the second index of a given character."""
        pass


if __name__ == '__main__':
    unittest.main()
