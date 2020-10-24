"""Test Werewolf object."""
from werewolf import Werewolf
from werewolf import Victim


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


def test_it_can_consume_victims_when_in_werewolf_form():
    """People can't consume victims, but werewolves can."""
    werewolf = Werewolf('David', 'London')
    victim = Victim()
    assert werewolf.human is True
    assert werewolf.consume(victim) == "I ain't no savage."
    werewolf.change()
    assert werewolf.human is False
    assert werewolf.consume(victim) == 'Nom Nom Nom'


def test_it_is_not_hungry_after_consuming_a_victim():
    """Werewolves get full when they have consumed a victim."""
    werewolf = Werewolf('David', 'London')
    victim = Victim()
    werewolf.change()
    assert werewolf.hungry is True
    werewolf.consume(victim)
    assert werewolf.hungry is False


def test_a_consumed_victims_status_is_dead():
    """Victims start out alive but die when they are consumed."""
    werewolf = Werewolf('David', 'London')
    victim = Victim()
    assert victim.status == 'alive'
    werewolf.change()
    werewolf.consume(victim)
    assert victim.status == 'dead'
