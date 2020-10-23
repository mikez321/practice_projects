"""Correct Sentence challenge from py.checkio.org."""
import unittest


def correct_sentence(sentence):
    return sentence


class SentenceTest(unittest.TestCase):
    """Testing for correct_sentence function."""

    def test_it_capitalizes_and_ends_the_sentence(self):
        """Sentences start with a capital letter and end with a period."""
        self.assertEqual(
            correct_sentence("greetings, friends"), "Greetings, friends.")


if __name__ == '__main__':
    unittest.main()
