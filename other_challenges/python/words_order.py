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
    phrase = phrase.split()
    for word in word_list:
        if word in phrase:
            phrase = phrase[phrase.index(word):]
        else:
            return False

    return True


class WordsOrderTest(unittest.TestCase):
    """Test for words_order function."""

    def test_basic_true(self):
        """Test words in order and in the phrase are True."""
        self.assertEqual(
            words_order('hi world im here', ['world', 'here']), True
        )

    def test_basic_false(self):
        """False if words not in phrase."""
        self.assertEqual(
            words_order('hi world im here', ['dog', 'lamb']), False
        )


if __name__ == '__main__':
    unittest.main()
