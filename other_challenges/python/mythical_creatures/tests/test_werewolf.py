"""Test Werewolf object."""
from werewolf import Werewolf


def test_it_exists():
    """Test that a werewolf object is created."""
    werewolf = Werewolf('David', 'London')
    assert type(werewolf) == Werewolf
