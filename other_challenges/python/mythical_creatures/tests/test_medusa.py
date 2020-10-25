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
    assert anna.statue_count() == 1


def test_max_three_victims():
    """Medusa can have 3 victims at a time and then they become unstoned."""
    rachel = Medusa('Rachel')
    max = Person('Max')
    agatha = Person('Agatha')
    jim = Person('Fishin Jim')
    lana = Person('Lana')
    rachel.stare_at(jim)
    rachel.stare_at(agatha)
    rachel.stare_at(max)
    assert jim.is_stoned() is True
    assert agatha.is_stoned() is True
    assert max.is_stoned() is True
    assert rachel.statue_count() == 3
    rachel.stare_at(lana)
    assert lana.is_stoned() is True
    assert rachel.statue_count() == 3
    assert jim.is_stoned() is False
