"""Character Jump Cassidoo Challenge."""
import unittest


def character_jump(skips: int, course: list) -> bool:
    """
    Retrun if a character can complete the course without hitting obstacles.

    :param skips: The number of items to be 'jumped over' at a time.
    :param course: A list of 1s and 0s.  1s represent an obstacle in a course.
        0s represent spaces in the course.
    :return: If the character is able to jump through the course over n number
        of spaces each time (represented by the variable skips) and never hit
        an obstacle, the function returns true.  If at any time the character
        will hit an obstacle, the function will return false.
    """
    if 1 in course[::skips]:
        return False

    return True


class CharacterJumpTest(unittest.TestCase):
    """Tests for character_jump function."""

    def test_it_passes_if_it_doesnt_hit_an_object(self):
        """True if it hits no obstacles."""
        self.assertEqual(character_jump(3, [0, 1, 0, 0, 0, 1, 0]), True)

    @unittest.skip('Pass first then fail.')
    def test_it_fails_if_it_hits_an_object(self):
        """False if it hits an obstacle."""
        self.assertEqual(character_jump(4, [0, 1, 1, 0, 1, 0, 0, 0, 0]), False)


if __name__ == '__main__':
    unittest.main()
