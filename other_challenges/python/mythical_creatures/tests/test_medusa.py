"""Tests for medusa.py."""
from medusa import Medusa
from medusa import Person


def test_it_exists():
    """Ensure barb is a medusa object."""
    barb = Medusa('Barb')
    assert type(barb) == Medusa


def test_it_has_a_name_and_no_statues_when_new():
    """New medusas have a name and no statues."""
    jane = Medusa('Jane')
    assert jane.get_name() == 'Jane'
    assert jane.statue_count() == 0


def test_stare_at_victim():
    """Stare at a victim adds victim to statue collection."""
    anna = Medusa('Anna')
    pete = Person('Pete')
    assert pete.is_stoned() is False
    anna.stare_at(pete)
    assert pete.is_stoned() is True
