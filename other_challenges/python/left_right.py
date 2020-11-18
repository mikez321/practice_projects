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


class LeftRightTest(unittest.TestCase):
    """Testing for leftright function."""

    def test_it_messes_up_instructions(self):
        """First test for leftright function."""
        self.assertEqual(
            left_join("left", "right", "left", "stop"), "left,left,left,stop")


if __name__ == '__main__':
    unittest.main()
