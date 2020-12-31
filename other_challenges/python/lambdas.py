"""Lambda exploration."""
import unittest


class LambdaTest(unittest.TestCase):
    """Tests go here."""

    def test_lambda_function(self):
        """Test number to a power lambda function."""
        self.assertEqual((lambda a, b: a**b)(2, 2), 4)
        self.assertEqual((lambda a, b: a**b)(2, 3), 8)
        self.assertEqual((lambda a, b: a**b)(4, 5), 1024)


if __name__ == "__main__":
    unittest.main()
