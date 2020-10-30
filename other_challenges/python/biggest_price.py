"""Bigger Price challenge from checkio.org."""
import unittest


def bigger_price(quantity: int, items: list) -> list:
    """
    Return the largest priced item in the list of items.

    :param quantity: The number of results to be returned.
    :param items: A list of dictionaries.  The name and price of each item.
    :return: A list is returned with the name and price of the most
        expensive items.  The number of items in this list is determined by
        the quantity param and the items in the list will be returned in
        decreasing order, with the first being the most expensive item in the
        complete list of items.
    """
    result = []

    for item in items:
        if len(result) == 0:
            result.append(item)
        elif result[0]['price'] < item['price']:
            result = [item] + result
        elif result[-1]['price'] > item['price']:
            result.append(item)
        else:
            for index, placed_item in enumerate(result):
                if placed_item['price'] > item['price']:
                    continue
                else:
                    new_index = index
                    result = (result[:new_index] + [item] + result[new_index:])
                    break

    return result[:quantity]


class PriceTest(unittest.TestCase):
    """Testing for bigger_price function."""

    def test_it_can_return_a_single_highest_price(self):
        """It can return the highest price of all items."""
        items = [
            {'name': 'pen', 'price': 5},
            {'name': 'whiteboard', 'price': 170},
        ]

        self.assertEqual(
            bigger_price(1, items), [{'name': 'whiteboard', 'price': 170}]
            )

    def test_it_can_return_a_list_of_n_items(self):
        """It will return n quantity of items ordered by price."""
        items = [
            {'name': 'pen', 'price': 5},
            {'name': 'asparagus', 'price': 2},
            {'name': 'dog', 'price': 500},
            {'name': 'whiteboard', 'price': 170},
        ]

        self.assertEqual(
            bigger_price(2, items), [
                    {'name': 'dog', 'price': 500},
                    {'name': 'whiteboard', 'price': 170},
                ]
            )

        self.assertEqual(
            bigger_price(3, items), [
                    {'name': 'dog', 'price': 500},
                    {'name': 'whiteboard', 'price': 170},
                    {'name': 'pen', 'price': 5}
                ]
            )


if __name__ == '__main__':
    unittest.main()
