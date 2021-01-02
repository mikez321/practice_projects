"""5 part password challenge from checkio."""
import unittest
# This was a 5 part password verification challenge from Checkio.org.
# I completed it, but here I will just copy/paste my code and start from the
# end.  I hope to be able to refactor it using tools I've learned over the
# past few days... lambdas and regex.

def is_acceptable_password(password: str) -> bool:
    return pass_length(password) and pass_numeric(password) and no_p_word(password) and three_unique_chars(password)

def pass_length(password):
    return len(password) >= 6

def pass_numeric(password):
    if len(password) > 9:
        return True

    nums = 0
    for char in list(password):
        if char.isnumeric():
            nums += 1
    if nums == 0 or len(password) == nums:
        return False

    return True

def no_p_word(password):
    if "password" in password.casefold():
        return False
    else:
        return True

def three_unique_chars(password):
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
