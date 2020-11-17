"""Popular words challenge from checkio."""
import unittest


def popular_words(text: str, words: list) -> dict:
    """
    Return word frequency in a given string of text.

    :param text: A string of text.
    :param words: A list of the words to be evaluated for frequency of
        occurance in the given text.
    :return: Function will return a dictionary with the keys being the words
        provided in the 'words' param and the values being the frequency that
        word appears in the given 'text' param.
    """


class PopularWordsTest(unittest.TestCase):
    """Testing for popular_words function."""

    def test_it_returns_words_by_popularity(self):
        """Return words and their popularity from a string."""
        self.assertEqual(popular_words(
            "When I was One I had just begun"
            "When I was Two I was nearly new", ['i', 'was', 'three', 'near']),
                {
                    'i': 4,
                    'was': 3,
                    'three': 0,
                    'near': 0
                }
        )


if __name__ == '__main__':
    unittest.main()
