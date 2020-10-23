"""Correct Sentence challenge from py.checkio.org."""
import unittest


def correct_sentence(text: str) -> str:
    """
    Capitalize the first letter of a sentence and end it with a period.

    :param text: A string that may or may not have proper capitalization
        and punctuation.
    :return: The original text string is returned with a capitalized first
        letter and a period to end it.  If the original text has proper
        punctuation and/or capitalization those will not be altered.
    """
    if text[-1] != '.':
        text += '.'

    if text[0].isalpha() and text[0].islower():
        capital_first = text[0].capitalize()
        text = capital_first + text[1:]

    return text


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

    def test_it_will_only_capitalize_the_first_letter(self):
        """If the sentence has proper nouns, those stay capitalized."""
        self.assertEqual(
            correct_sentence("welcome to New York"), "Welcome to New York.")


if __name__ == '__main__':
    unittest.main()
