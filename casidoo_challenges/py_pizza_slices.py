"""Cassidoo Challenge - Gimme Pizza."""
import unittest
import math


def get_slices(person):
    """Return the number of slices of pizza wanted by a person."""
    return person.pizza_slices


def gimme_pizza(people: list, slices: int) -> int:
    """
    Return the number of pizzas that need to be ordered.

    :param people: A list of person objects.  Each person has a name and
        the number of slices of pizza they are hungry for.
    :param slices: An int that represents how many slices a pizza is cut
        into.
    :return: Returns the number of pizzas that should be ordered to give
        everyone their desired slices of pizza.
    """
    total_slices = sum(map(get_slices, people))
    pizzas = total_slices / slices

    return math.ceil(pizzas)


class Person(object):
    """This represents a person and how many pizza slices they want."""

    def __init__(self, name, pizza_slices):
        """
        Person object with name and pizza slices desired.

        :param name: str: The person's name
        :param pizza_slices: int: The number of slices of pizza that person
            wants to eat.  This is important for calculating the number of
            pizzas that should be ordered.
        """
        self.name = name
        self.pizza_slices = pizza_slices


class TestGimmePizza(unittest.TestCase):
    """Testing for gimme_pizza function."""

    def test_it_knows_how_many_slices_to_give(self):
        """It will reutrn how many pizzas to order."""
        mike = Person('Mike', 4)
        erin = Person('Erin', 3)
        charlotte = Person('Charlotte', 8)
        sydney = Person('Sydney', 3)

        arr = [mike, erin, charlotte, sydney]

        self.assertEqual(gimme_pizza(arr, 8), 3)

        hungry_pup = [charlotte]

        self.assertEqual(gimme_pizza(hungry_pup, 8), 1)

    def test_show_how_many_slices_of_pizza_a_person_wants(self):
        """Return the number of slices of pizza a person wants."""
        mike = Person('Mike', 4)

        self.assertEqual(get_slices(mike), 4)


if __name__ == '__main__':
    unittest.main()
