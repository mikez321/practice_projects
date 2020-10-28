"""Three words challenge from checkio.org."""
import unittest


def three_words(text: str) -> bool:
    """
    Given a string of text return true if it contains 3 successive words.

    :param text: A string of text.  The text does not contain any numbers.
    :return:  If the string contains 3 words in succession the function
        returns true, otherwise it will return false.
    """
    cons_alpha = 0
    for word in text.split():
        if word.isalpha():
            cons_alpha += 1
            if cons_alpha == 3:
                return True
        else:
            cons_alpha = 0

    return False


class ThreeWordsTest(unittest.TestCase):
    """Testing for three words function."""

    def test_it_returns_true_if_there_are_3_words_in_succession(self):
        """Return true if 3 words are in succession."""
        self.assertEqual(three_words('Hello World hello'), True)
        # self.assertEqual(three_words('He is 123 man'), False)


if __name__ == '__main__':
    unittest.main()
