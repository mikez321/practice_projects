"""First word challenge from checkio."""
import unittest


def first_word(text: str) -> str:
    """
    Return the first word of a given string.

    :param text: Any string of text.
    :return: The first word in that string of text is returned. If there is an
        apostrophe and it is part of the word it should be included.  Erroneous
        punctuation before or after a word should be removed.
    """
    first_word = list(text.split()[0])

    indexes = len(first_word)

    for index in reversed(range(0, indexes)):
        if first_word[index].isalpha() is False:
            del first_word[index]

    return "".join(first_word)


class FirstWordTest(unittest.TestCase):
    """Testing for first word function."""

    def test_it_returns_the_first_word(self):
        """Function returns the first word of a given string."""
        self.assertEqual(first_word("Hello world"), "Hello")

    def test_it_removes_starting_or_ending_punctuation(self):
        """Remove comma at end of this example."""
        self.assertEqual(first_word("greetings, friends"), "greetings")

    # def test_it_can_remove_lots_of_punctuation(self):
    #     """It can remove lots of punctuation on either side."""
    #     self.assertEqual(first_word("... and so on ..."), "and")


if __name__ == '__main__':
    unittest.main()
