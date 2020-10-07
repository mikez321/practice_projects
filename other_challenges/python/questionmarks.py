"""Question Mark Challenge."""
import unittest


def question_marks(code: str) -> bool:
    """
    Determine if a passed in string meets the requirements and return boolean.

    :param code: This is a string of single digit numbers, letters and question
        marks.
    :return: This function will return True if there are 3 question marks
        between every pair of two numbers that add up to 10.  If there are no
        two numbers that add to 10, the function will return False.

    :Example:
        question_marks("arrb6???4xxbl5???eee5") will return True because there
        are 3 question marks between 6 and 4, and also three question marks
        between 5 and 5.
    """
    pass


class QuestionMarkTest(unittest.TestCase):
    """Testing for Question Mark challenge."""

    def test_it_passes_the_pattern(self):
        """It can identify if the passed in string adheres to the pattern."""
        self.assertTrue(question_marks("acc?7??sss?3rr1??????5"))


if __name__ == '__main__':
    unittest.main()
