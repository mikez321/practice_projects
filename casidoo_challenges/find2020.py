"""Find 2020 if it exists."""
import unittest


def find2020(number: str) -> int:
    """
    Find the index position of '2020' in a string.

    :param number: A string of 0 and 2.  It may or may not contain '2020'.
    :result: If '2020' is in the given string, retun its starting index
        position.  If it is not in the string, return -1.
    """
    # This is probably how I'd use it IRL, but the instructions said no use
    # of .index() type of methods.
    # try:
    #     return number.index('2020')
    # except ValueError:
    #     return -1
    count = 0
    while len(number) > 3:
        if number[:4] == '2020':
            return count
        else:
            count += 1
            number = number[1:]

    return -1


class TwentTwentyTest(unittest.TestCase):
    """Testing for 2020 function."""

    def test_setup(self):
        """Test unittest setup with 1 == 1."""
        self.assertEqual(1, 1)

    def test_empty_string_is_minus_one(self):
        """An empty string evaluates to -1."""
        self.assertEqual(find2020(''), -1)

    def test_a_single_number_is_minus_one(self):
        """A single number also evaluates to -1."""
        self.assertEqual(find2020('2'), -1)

    def test_find_2020(self):
        """Return -1 if 2020 not in string or index if it is."""
        self.assertEqual(find2020('0000'), -1)
        self.assertEqual(find2020('20002020'), 4)


if __name__ == '__main__':
    unittest.main()
