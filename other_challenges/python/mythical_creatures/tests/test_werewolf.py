"""Test Werewolf object."""
from werewolf import Werewolf


def test_it_exists():
    """Test that a werewolf object is created."""
    werewolf = Werewolf()
    assert type(werewolf) == Werewolf


def test_it_has_attributes():
    """Test that a werewolf has a name and location."""
    werewolf = Werewolf()
    werewolf.name = 'David'
    werewolf.location = 'London'
    assert werewolf.name == 'David'
    assert werewolf.location == 'London'


def test_it_is_human_by_default():
    """Test that a werewolf starts off human."""
    werewolf = Werewolf()
    werewolf.name = 'David'
    werewolf.location = 'London'
    assert werewolf.is_human() is True


def test_it_can_change_into_a_werewolf():
    """Test that the change method makes it a werewolf."""
    werewolf = Werewolf()
    werewolf.name = 'David'
    werewolf.location = 'London'
    werewolf.change()
    assert werewolf.is_human() is False
