"""Test for Dragon object."""
from dragon import Dragon


def test_it_has_a_name():
    """Test that a dragon has a name."""
    tom = Dragon('Tom')
    assert tom.name == 'Tom'
