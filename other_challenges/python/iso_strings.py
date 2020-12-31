"""Surjection Strings challenge from checkio."""
import unittest


def isometric_strings(str1: string, str2: string) -> bool:
    """
    Return true if string1 and string2 are isometric.
    :example:
        add and egg are isometric because you can set a=e and d=g and they will
        spell out the two words respectively.
        Conversely, foo and bar are not isometric, because you can not swap out
        any one letter for another and make new words.
        isometric_strings('add', 'egg')
        >>> True
        isometric_strings('foo', 'bar')
        >>> False
    """


class IsoStringsTest(unittest.TestCase):
    """Testing for iso_strings function."""

    def test_basic_true(self):
        """Set up testing."""
        self.assertEqual(1, 1)

    def test_egg(self):
        """Egg and Add are isometric strings."""
        self.assertEqual(isometric_strings('add', 'egg'), True)


if __name__ == '__main__':
    unittest.main()
