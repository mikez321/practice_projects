"""Correct Sentence challenge from py.checkio.org."""
import unittest


def correct_sentence(sentence: str) -> str:
    """
    Capitalize the first letter of a sentence and end it with a period.

    :param sentence: A string that may or may not have proper capitalization
        and punctuation.
    :return: The original sentence string is returned with a capitalized first
        letter and a period to end it.  If the original sentence has proper
        punctuation and/or capitalization those will not be altered.
    """
    if sentence[-1] != '.':
        sentence += '.'

    return sentence.capitalize()


class SentenceTest(unittest.TestCase):
    """Testing for correct_sentence function."""

    def test_it_capitalizes_and_ends_the_sentence(self):
        """Sentences start with a capital letter and end with a period."""
        self.assertEqual(
            correct_sentence("greetings, friends"), "Greetings, friends.")

    def test_it_will_not_add_additional_periods_if_it_has_one(self):
        """If the sentence already has a period another will not be added."""
        self.assertEqual(
            correct_sentence("greetings, friends."), "Greetings, friends.")

    def test_it_will_not_have_issues_if_the_first_letter_is_capitalized(self):
        """If the sentence already begins capitalized it is fine."""
        self.assertEqual(
            correct_sentence("Greetings, friends"), "Greetings, friends.")

    def test_the_original_sentence_will_be_returned_if_it_is_correct(self):
        """If the sentence is fine it will be unchanged."""
        self.assertEqual(
            correct_sentence("Greetings, friends"), "Greetings, friends.")


if __name__ == '__main__':
    unittest.main()
