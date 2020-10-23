"""Correct Sentence challenge from py.checkio.org."""


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
