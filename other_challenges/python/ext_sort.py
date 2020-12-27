"""Sort by extension challenge from checkio."""
import unittest


def sort_by_ext(files: list) -> list:
    """
    Given a list of files sort them by their extension.

    :param files: A list of strings representing file names and extensions.
    :return: Return the list sorted by file extension in alphabetical
        order, and if files have the same extension, they should be sorted by
        file name in alphabetical order.
    """
    result = []
    separated_names = {}
    for file in files:
        split_file = file.split(".")
        if len(split_file) > 2:
            name = ".".join(split_file[:-1])
            ext = split_file[-1]
        else:
            name = split_file[0]
            ext = split_file[1]

        if separated_names.get(ext) is None:
            separated_names[ext] = [name]
        else:
            separated_names[ext].append(name)

    for extension in sorted(separated_names.keys()):
        for file in separated_names[extension]:
            result.append(f"{file}.{extension}")

    return result


class ExtSortTest(unittest.TestCase):
    """Testing for sort_by_ext function."""

    def test_it_sorts_by_file_extension(self):
        """It sorts by file extension."""
        self.assertEqual(
            sort_by_ext(['1.cad', '1.bat', '1.aa']), ['1.aa', '1.bat', '1.cad']
        )

    def test_it_can_have_no_extension(self):
        """It can process files with no file extension."""
        self.assertEqual(
            sort_by_ext(['1.cad', '1.', '1.aa']), ['1.', '1.aa', '1.cad']
        )

    def test_multiple_files_with_same_ext(self):
        """If multiple files have the same ext they are sorted alphabetical."""
        self.assertEqual(
            sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']), ['1.aa', '1.bat', '2.bat', '1.cad']
        )

    def test_punctuation_in_filename(self):
        """'table.imp.xls' has an extension 'xls' and a name 'table.imp'"""
        self.assertEqual(
            sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']), ['1.aa', '1.bat', '1.cad', '1.aa.doc']
        )

if __name__ == '__main__':
    unittest.main()
