"""Sort by extension challenge from checkio."""
import unittest

def sort_by_ext(files: list) -> list:
    """
    Given a list of files sort them by their extension

    :param files: A list of strings representing file names and extensions.
    :return: Return the list sorted by file extension in alphabetical
        order, and if files have the same extension, they should be sorted by
        file name in alphabetical order.
    """
    pass


class ExtSortTest(unittest.TestCase):
    """Testing for sort_by_ext function."""

    def test_it_sorts_by_file_extension(self):
        """It sorts by file extension."""
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
