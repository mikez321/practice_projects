"""Surjection Strings challenge from checkio."""
import unittest


def isometric_strings(str1: str, str2: str) -> bool:
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
    pattern1 = map(lambda i: str1.index(i), str1)
    pattern2 = map(lambda i: str2.index(i), str2)

    return list(pattern1) == list(pattern2)



class IsoStringsTest(unittest.TestCase):
    """Testing for iso_strings function."""

    def test_basic_true(self):
        """Set up testing."""
        self.assertEqual(1, 1)

    def test_egg(self):
        """Egg and Add are isometric strings."""
        self.assertEqual(isometric_strings('add', 'egg'), True)

    def test_foo(self):
        """Foo and Bar are not isometric strings."""
        self.assertEqual(isometric_strings('foo', 'bar'), False)

    def test_empty(self):
        """Empty strings are isometric."""
        self.assertEqual(isometric_strings('', ''), True)

    def test_same_strings(self):
        """Two equal strings are isometric."""
        self.assertEqual(isometric_strings('all', 'all'), True)

    def test_isomorphic(self):
        """Strings must have the same pattern to be isometric."""
        self.assertEqual(isometric_strings('hall', 'hoop'), False)

if __name__ == '__main__':
    unittest.main()
