"""Find the longest word in a given string."""
import unittest


def longest_word(sen: str) -> str:
    """
    Find the longest word in a space separated string.

    :param sen: A space separated string of words.  This can also include
        punctuation, but punctuation will be ignored.
    :return: The longest string in sen(punctuation will be ignored).  If two
        strings are the same length, the first will be returned.
    """
    longest_word = 0
    longest_index = None

    split_words = sen.split()

    for index, word in enumerate(split_words):
        alphas = 0
        for letter in word:
            if letter.isalpha() or letter.isnumeric():
                alphas += 1
        if alphas > longest_word:
            longest_word, longest_index = alphas, index

    return split_words[longest_index]


class LongestWordTest(unittest.TestCase):
    """Testing for longest word function."""

    def test_it_knows_the_longest_word(self):
        """Return the longest word excluding punctuation."""
        self.assertEqual(longest_word('I love dogs'), 'love')
        self.assertEqual(longest_word('I love #dogs!!!!'), 'love')
        self.assertEqual(longest_word('123456789 98765432'), '123456789')


if __name__ == '__main__':
    unittest.main()
