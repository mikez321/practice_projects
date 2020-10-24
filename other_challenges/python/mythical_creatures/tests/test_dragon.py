"""Test for Dragon object."""
from dragon import Dragon


def test_it_exists():
    """Test that the object is created."""
    dan = Dragon('Dan', 'Gold', 'James')
    assert type(dan) == Dragon


def test_it_has_a_name_and_color():
    """Test that a dragon has a name."""
    tom = Dragon('Tom', 'Gold', 'Ben')
    assert tom.get_name() == 'Tom'
    assert tom.get_color() == 'Gold'


def test_it_has_a_rider():
    """A dragon has a rider with a name."""
    elise = Dragon('Elise', 'Green', 'Lessa')
    assert elise.get_rider() == 'Lessa'


def test_dragons_are_born_hungry():
    """When a dragon is born it is hungry."""
    gretchen = Dragon('Gretchen', 'Yellow', 'Lacey')
    assert gretchen.is_hungry() is True


def test_dragons_eat_a_lot():
    """If a dragon eats more than 3 times, it will no longer be hungry."""
    regina = Dragon('Regina', 'Red', 'Rachel')
    assert regina.is_hungry() is True
    regina.eat()
    regina.eat()
    regina.eat()
    assert regina.is_hungry() is True
    regina.eat()
    assert regina.is_hungry() is False
