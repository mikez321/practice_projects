"""Second index challenge from checkio."""
import unittest


def second_index(text: str, target: str) -> [int, None]:
    """
    Return the index of the second instance of a given character.

    :param text: Any string of text, numbers, characters.
    :target: The 'target' character.  The function will give the index of the
        second occurance of this character.
    :return: The index position of the second instance of the target will be
        returned.  If there is not a second instance of this character the
        function will return None.
    """
    found = 0

    for index, char in enumerate(text):
        if char.casefold() == target.casefold() and found == 1:
            return(index)
        elif char.casefold() == target.casefold():
            found += 1


class QuestionMarkTest(unittest.TestCase):
    """Testing for Second Index challenge."""

    def test_it_returns_the_second_index_of_the_char(self):
        """It will return the second index of a given character."""
        self.assertEqual(second_index("sims", "s"), 3)
        self.assertEqual(second_index("find the river", "e"), 12)
        self.assertEqual(second_index("hi", " "), None)
        self.assertEqual(second_index("three occurrences", "r"), 10)


if __name__ == '__main__':
    unittest.main()
