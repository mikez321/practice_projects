"""Bigger Price challenge from checkio.org."""
import unittest


def bigger_price(quantity: int, items: list) -> list:
    """
    Return the largest priced item in the list of items.

    :param quantity: The number of results to be returned.
    :param items: A list of dictionaries.  The name and price of each item.
    :return: A list is returned with the name and price of the most
        expensive items.  The number of items in this list is determined by
        the quanity param and the items in the list will be returned in
        decreasing order, with the first being the most expensive item in the
        complete list of items.
    """


class PriceTest(unittest.TestCase):
    """Testing for bigger_price function."""

    def test_it_can_return_a_single_highest_price(self):
        """It can return the highest price of all items."""
        items = [
            {'name': 'pen', 'price': 5},
            {'name': 'whiteboard', 'price': 170},
        ]

        self.assertEqual(
            bigger_price(1, items), {'name': 'whiteboard', 'price': 170}
            )


if __name__ == '__main__':
    unittest.main()
