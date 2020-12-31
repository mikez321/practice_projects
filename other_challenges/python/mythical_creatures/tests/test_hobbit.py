"""Testing for hobbit.py."""
from hobbit import Hobbit


def test_it_exists():
    """New hobbits have names and attributes."""
    dan = Hobbit("Dan")
    assert type(dan) == Hobbit
    assert dan.name == "Dan"
    assert dan.disposition == "adventurous"
    assert dan.age == 0


def test_it_ages():
    """A hobbit ages when it has a birthday."""
    blake = Hobbit("Blake")
    assert blake.age == 0

    for _ in range(0, 5):
        blake.celebrate_birthday()

    assert blake.age == 5
    assert blake.is_adult() is False

    for _ in range(0, 28):
        blake.celebrate_birthday()

    assert blake.age == 33
    assert blake.is_adult() is True

    blake.celebrate_birthday()

    assert blake.age == 34
    assert blake.is_adult() is True


def test_it_can_be_old():
    """A hobbit is old when it is 101 years old."""
    larry = Hobbit("Larry")
    larry.age = 100
    assert larry.is_adult() is True
    assert larry.is_old() is False
    larry.celebrate_birthday()
    assert larry.is_old() is True


def test_can_have_a_ring():
    """A hobbit named Danielle has a ring."""
    ben = Hobbit("Ben")
    danielle = Hobbit("Danielle")
    stacy = Hobbit("Stacy")
    assert ben.has_ring() is False
    assert stacy.has_ring() is False
    assert danielle.has_ring() is True


def test_is_short():
    """Hobbits are short."""
    tracy = Hobbit("Tracy")
    assert tracy.is_short() is True
