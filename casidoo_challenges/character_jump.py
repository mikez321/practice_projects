"""Character Jump Cassidoo Challenge."""
import unittest


class CharacterJumpTest(unittest.TestCase):
    """Tests for char_jump function."""

    def test_it_passes_if_it_doesnt_hit_an_object(self):
        """True if it hits no obstacles."""
        self.assertEqual(character_jump(3, [0, 1, 0, 0, 0, 1, 0]))

    @unittest.skip('Pass first then fail.')
    def test_it_fails_if_it_hits_an_object(self):
        """False if it hits an obstacle."""
        self.assertEqual(character_jump(4, [0, 1, 1, 0, 1, 0, 0, 0, 0]))


if __name__ == '__main__':
    unittest.main()
