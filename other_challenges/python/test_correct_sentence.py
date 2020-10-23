"""Testing for correct sentence function."""
from correct_sentence import correct_sentence


def test_it_capitalizes_and_ends_the_sentence():
    """Sentences start with a capital letter and end with a period."""
    assert correct_sentence('greetings, friends') == "Greetings, friends."


def test_it_will_not_add_additional_periods_if_it_has_one():
    """If the sentence already has a period another will not be added."""
    assert correct_sentence("greetings, friends.") == "Greetings, friends."


def test_it_will_not_have_issues_if_the_first_letter_is_capitalized():
    """If the sentence already begins capitalized it is fine."""
    assert correct_sentence("Greetings, friends") == "Greetings, friends."


def test_the_original_sentence_will_be_returned_if_it_is_correct():
    """If the sentence is fine it will be unchanged."""
    assert correct_sentence("Greetings, friends") == "Greetings, friends."


def test_it_will_only_capitalize_the_first_letter():
    """If the sentence has proper nouns, those stay capitalized."""
    assert correct_sentence("welcome to New York") == "Welcome to New York."
