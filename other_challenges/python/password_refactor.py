"""5 part password challenge from checkio."""
import unittest
import re
from IPython import embed
# This was a 5 part password verification challenge from Checkio.org.
# I completed it (not too difficult) but here I'll do some refactoring using
# Python/other things I've learned about over my Christmas/New Years break:
# lambdas, ternerary operators and  regex.


def is_acceptable_password(password: str) -> bool:
    """Return true if all criteria for passwords are met."""
    acceptable_password = all([
        pass_length(password),
        pass_numeric(password),
        no_p_word(password),
        three_unique_chars(password),
    ])

    return acceptable_password


def pass_length(password):
    """Length of password must be at least 6 chars."""
    return len(password) >= 6


def pass_numeric(password):
    """Return true if it has a digit but false if all digits."""
    if len(password) > 9:
        return True

    if re.search("\d", password) and re.search("[A-z]", password):
        return True
    else:
        return False


def no_p_word(password):
    """Return false if it contains password in any case."""
    if "password" in password.casefold():
        return False
    else:
        return True


def three_unique_chars(password):
    """Return false if there are not at least 3 unique characters."""
    if len(set(password)) >= 3:
        return True

    return False


class PasswordCheckTest(unittest.TestCase):
    """Testing for checkio password checker."""

    def test_setup(self):
        """Check that test is set up properly."""
        self.assertEqual(1, 1)

    def test_length(self):
        """Password must be longer than 6 chars."""
        self.assertEqual(is_acceptable_password('short'), False)
        self.assertEqual(is_acceptable_password('short54'), True)
        self.assertEqual(is_acceptable_password('muchlonger'), True)

    def test_has_digit(self):
        """Password must have at least one digit but can not be only digits."""
        self.assertEqual(is_acceptable_password('ashort'), False)
        self.assertEqual(is_acceptable_password('1234567'), False)
        self.assertEqual(is_acceptable_password('muchlonger5'), True)

    def test_digit_rules(self):
        """If longer than 9 it can contain none or all digits."""
        self.assertEqual(is_acceptable_password('sh5'), False)
        self.assertEqual(is_acceptable_password('1234567'), False)
        self.assertEqual(is_acceptable_password('12345678910'), True)

    def test_no_p_word(self):
        """Password can not contain word password in any case."""
        self.assertEqual(is_acceptable_password('password12345'), False)
        self.assertEqual(is_acceptable_password('PASSWORD12345'), False)
        self.assertEqual(is_acceptable_password('pass1234word'), True)

    def test_unique_chars(self):
        """Password must contain more than 3 characters."""
        self.assertEqual(is_acceptable_password('aaaaaa1'), False)
        self.assertEqual(is_acceptable_password('aaaaaabbbbb'), False)


if __name__ == "__main__":
    unittest.main()
