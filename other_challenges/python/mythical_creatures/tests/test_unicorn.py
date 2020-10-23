"""Testing for unicorn.py."""
from unicorn import Unicorn


def test_it_has_a_name():
    """A unicorn will be created with a name."""
    rob = Unicorn('Robert')
    assert rob.name == 'Robert'


# def test_it_is_white_by_default():
#     """Unicorns are white by default."""
#     rob = Unicorn('Robert')
#     assert rob.color == 'White'
