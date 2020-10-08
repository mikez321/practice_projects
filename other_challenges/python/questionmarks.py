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
    tens = []
    num_1 = None
    index_1 = None

    for index, char in enumerate(code):
        if char.isnumeric() and num_1 is None:
            num_1, index_1 = int(char), index
        elif char.isnumeric():
            if num_1 + int(char) == 10:
                tens.append((index_1, index))
            num_1, index_1 = int(char), index

    if len(tens) == 0:
        return False
    else:
        for index_pair in tens:
            snippet = code[index_pair[0]: index_pair[-1]]
            if snippet.count('?') != 3:
                return False
                break

        return True


class QuestionMarkTest(unittest.TestCase):
    """Testing for Question Mark challenge."""

    def test_it_passes_the_pattern(self):
        """It can identify if the passed in string adheres to the pattern."""
        self.assertEqual(question_marks("acc?7??sss?3rr1??????5"), True)
        self.assertEqual(question_marks("aa6?9"), False)


if __name__ == '__main__':
    unittest.main()
