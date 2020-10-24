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
