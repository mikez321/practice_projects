"""FirstFactorial challenge from Coderbyte."""
import unittest


def first_factorial(num: int, result: int = 1) -> int:
    """
    Calculate the factoral of a number.

    :param num: A positive integer
    :param result: Default value of 1, but will increment in recursive function
    :result: The factoral of that number

    :Example:
    FirstFactoral(4)
      (4 * 3 * 2 * 1 = 24)

    >> 24
    """
    if num == 0:
        return result
    else:
        return first_factorial((num - 1), (num * result))


class FirstFactorialTest(unittest.TestCase):
    """Testing for factorial function."""

    def test_it_calculates_factorials(self):
        """Return the factorial of a given number."""
        self.assertEqual(first_factorial(4), 24)
        self.assertEqual(first_factorial(5), 120)
        self.assertEqual(first_factorial(12), 479001600)


if __name__ == '__main__':
    unittest.main()
