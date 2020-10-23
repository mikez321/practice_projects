"""Testing for vampire object."""
from vampire import Vampire


def test_it_has_a_name():
    """Vampires are given names when they are created."""
    vampire = Vampire("Dracula")
    assert vampire.name == "Dracula"


def test_it_is_named_something_else():
    """Vampires can have different names."""
    vampire = Vampire("Vladimir")
    assert vampire.name == "Vladimir"


def test_it_keeps_a_pet_bat_by_default():
    """Defaults to having a pet bat."""
    vampire = Vampire("Ruthven")
    assert vampire.pet == "bat"


def test_it_can_have_other_pets():
    """Can have a different kind of pet."""
    vampire = Vampire("Varney", "fox")
    assert vampire.pet == "fox"


def test_it_is_thirsty_by_default():
    """Vampires are thirsty by default."""
    vampire = Vampire("Count von Count")
    assert vampire.is_thirsty() is True


def test_it_is_not_thirsty_after_drinking():
    """After it drinks it is not thirsty anymore."""
    vampire = Vampire("Elizabeth Bathory")
    vampire.drink()
    assert vampire.is_thirsty() is False
