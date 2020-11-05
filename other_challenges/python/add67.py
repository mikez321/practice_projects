"""Add all numbers not enclosed in 6 and 7."""
import unittest


def add67(nums: list) -> int:
    """
    Add together any numbers not enclosed in 6 and 7.

    :param nums: A list of ints
    :return: The sum of all numbers not enclosed in 6 and 7.  Adding will stop
        when the number 6 is reached, and it will not continue until after the
        next number 7 is found.
    :example:
        add67[1, 2, 3]
        >>> 6

        add67[1, 2, 6, 5, 7, 3]
        >>> 6
    """
    running_sum = 0
    if 6 not in nums:
        return sum(nums)
    else:
        omit = False
        for num in nums:
            if omit is False and num != 6:
                running_sum += num
            elif omit is False and num == 6:
                omit = True
                continue
            elif omit is True and num == 7:
                omit = False
                continue

    return running_sum


class Add67Test(unittest.TestCase):
    """Testing for add67 function."""

    def test_it_adds_numbers(self):
        """If no 6s are present, it will add the numbers."""
        self.assertEqual(add67([1, 2, 3]), 6)

    def test_it_wont_add_nums_enclosed_in_6_and_7(self):
        """Numbers between 6 and 7s wont be added."""
        self.assertEqual(add67([1, 6, 2, 3, 7]), 1)

    def test_6s_and_7s_can_be_anywhere(self):
        """7s can  be added and can be in more than 1 place."""
        self.assertEqual(add67([7, 1, 6, 7, 2, 6, 5, 6, 7, 7]), 17)


if __name__ == '__main__':
    unittest.main()
