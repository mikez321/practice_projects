"""FirstFactorial challenge from Coderbyte."""
import unittest


def first_factorial(num: int) -> int:
    """
    Calculate the factoral of a number.

    :param num: A positive integer
    :result: The factoral of that number

    :Example:
    FirstFactoral(4)
      (4 * 3 * 2 * 1 = 24)

    >> 24
    """
    result = 1
    nums = list(range(1, num + 1))
    while len(nums) > 0:
        result *= nums[-1]
        nums = nums[:-1]

    return result


class FirstFactorialTest(unittest.TestCase):
    """Testing for factorial function."""

    def test_it_calculates_factorials(self):
        """Return the factorial of a given number."""
        self.assertEqual(first_factorial(4), 24)
        self.assertEqual(first_factorial(5), 120)
        self.assertEqual(first_factorial(12), 479001600)


if __name__ == '__main__':
    unittest.main()
