"""Lambda exploration."""
import unittest


power_fun = lambda a, b: a ** b


class LambdaTest(unittest.TestCase):
    """Tests go here."""

    def test_lambda_function(self):
        """Test number to a power lambda function."""
        self.assertEqual(power_fun(2, 3), 8)
        self.assertEqual(power_fun(4, 5), 1024)


if __name__ == "__main__":
    unittest.main()
