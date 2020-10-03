"""Cassidoo Challenge - Gimme Pizza."""
import unittest
# Given an array of people objects (where each person has a name and a number
# of pizza slices they’re hungry for) and a number for the number of slices
# that the pizza can be sliced into, return the number of pizzas you need to
# buy.
#
# Example:
#
# $ arr = [
#     { name: Joe, num: 9 },
#     { name: Cami, num: 3 },
#     { name: Cassidy, num: 4 }
# ]
# $ gimmePizza(arr, 8)
# $ 2 // 16 slices needed, pizzas can be sliced into 8 pieces, so 2 pizzas
# should be ordered


class TestGimmePizza(unittest.TestCase):
    """Testing for gimme_pizza function."""

    def test_it_knows_how_many_slices_to_give(self):
        """It will reutrn how many pizzas to order."""
        self.assertEqual(gimme_pizza(arr, 8), 2)
