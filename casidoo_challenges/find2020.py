"""Find 2020 if it exists."""
import unittest


def find2020(number: str) -> int:
    """
    Find the index position of '2020' in a string.

    :param number: A string of 0 and 2.  It may or may not contain '2020'.
    :result: If '2020' is in the given string, retun its starting index
        position.  If it is not in the string, return -1.
    """


class TwentTwentyTest(unittest.TestCase):
    """Testing for 2020 function."""

    def test_setup(self):
        """Test unittest setup with 1 == 1."""
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
