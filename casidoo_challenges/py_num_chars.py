"""Casidoo challenge for number of characters."""
import unittest
# Given a string s and a character c, return the number of occurrences
# of c in s.
# Ex: num_chars('oh heavens', 'h')
# => 2


def num_chars(phrase, letter):
    """Count the number of a given letter in a phrase."""
    return phrase.count(letter)


class NumCharsTest(unittest.TestCase):
    """Testing for num_chars function."""

    def test_it_knows_how_many_given_characters_are_in_a_string(self):
        """Return how many times a letter appears in a string."""
        self.assertEqual(num_chars('oh_heavens', 'h'), 2)
        self.assertEqual(num_chars('she sells seashells down by the seashore',
                                   's'), 8)


if __name__ == '__main__':
    unittest.main()
