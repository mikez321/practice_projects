"""Test Werewolf object."""
from werewolf import Werewolf


def test_it_exists():
    """Test that a werewolf object is created."""
    werewolf = Werewolf('David', 'London')
    assert type(werewolf) == Werewolf


def test_it_has_attributes():
    """Test that a werewolf has a name and location."""
    werewolf = Werewolf('David', 'London')
    assert werewolf.name == 'David'
    assert werewolf.location == 'London'


def test_it_is_human_by_default():
    """Test that a werewolf starts off human."""
    werewolf = Werewolf('David', 'London')
    assert werewolf.human is True


def test_it_can_change_into_a_werewolf():
    """Test that the change method makes it a werewolf."""
    werewolf = Werewolf('David', 'London')
    werewolf.change()
    assert werewolf.human is False


def test_it_can_cange_back_into_human_form():
    """If a werewolf is in wolf form and changes it becomes human."""
    werewolf = Werewolf('David', 'London')
    assert werewolf.human is True
    werewolf.change()
    assert werewolf.human is False
    werewolf.change()
    assert werewolf.human is True


def test_it_is_hungry_when_it_becomes_a_werewolf():
    """Werewolves are hungry, humans are not."""
    werewolf = Werewolf('David', 'London')
    assert werewolf.human is True
    assert werewolf.hungry is False
    werewolf.change()
    assert werewolf.human is False
    assert werewolf.hungry is True
