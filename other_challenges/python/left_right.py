"""Left Right challenge from check.io."""
import unittest


def left_join(phrases: tuple) -> str:
    """
    Return a single string from a tuple of strings.

    :param prhases:  A tuple of strings
    :return: All strings returned as a single, comma separated string.
        However, in the return, any instance of 'right' should be replaced
        with 'left' even if it is in the middle of a word.
    :example:
        left_join(("bright aright", "ok"))
        >>> "bleft aleft,ok"
    """
    result = []
    for word in phrases:
        if 'right' in word:
            result.append(replace_right(word))
        else:
            result.append(word)

    return ",".join(result)


def replace_right(word):
    """Replace any instance of 'right' with 'left'."""
    if 'right' in word:
        start_chop = word.index('right')
        end_chop = start_chop + len('right')
        new_word = word[:start_chop] + 'left' + word[end_chop:]
        return replace_right(new_word)
    else:
        return word


class LeftRightTest(unittest.TestCase):
    """Testing for leftright function."""

    def test_it_replaces_words(self):
        """It replaces the word right with the word left."""
        self.assertEqual(replace_right('right'), 'left')

    def test_it_replaces_right_multiple_times(self):
        """It can replace right more than once per word."""
        self.assertEqual(
            replace_right('alright rightoh right on'), 'alleft leftoh left on'
        )

    def test_it_messes_up_instructions(self):
        """It replaced "left" for any instance of the word "right"."""
        self.assertEqual(
            left_join(("left", "right", "left", "stop")), "left,left,left,stop"
        )

    def test_it_can_replace_part_of_a_word(self):
        """It can replace part of a word."""
        self.assertEqual(
            left_join(("bright aright", "ok")), "bleft aleft,ok"
        )


if __name__ == '__main__':
    unittest.main()
