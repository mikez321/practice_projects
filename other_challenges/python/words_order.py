import unittest

def words_order(phrase: str, word_list: list) -> bool:
    """
    Return True if all words in word_list are unique and in order in phrase.

    :param phrase: Any string of english words.
    :param word_lsit: A list of words which may or may not bein in the phrase
    :return: If the words in word_list are found in phrase and are in the same
        order in phrase as they are in the list AND no two words are both in
        the word list, the function should return True.  Words are case
        sensitive.
    :example:
        words_order('hi world im here', ['world', 'here'])
        >> True
        words_order('hi world im here', ['here', 'world'])
        >> False
        words_order('hi world im here', ['world', 'world'])
        >> False
    """


class WordsOrderTest(unittest.TestCase):
    """Test for words_order function."""

    def test_setup(self):
        """Test unittest is set up properly."""
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
