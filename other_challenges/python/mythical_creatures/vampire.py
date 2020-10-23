"""Vampire object from Turing's Mythical Creatures."""


class Vampire:
    """Vampire class that wants to suck your blood."""

    def __init__(self, name, pet='bat'):
        """Initialize a vampire objet with a name and a pet bat."""
        self.name = name
        self.pet = pet
        self.thirst = 0

    def is_thirsty(self):
        """Return boolean of thirsty or not."""
        if self.thirst == 0:
            return True
        else:
            return False

    def drink(self):
        """Change default thirst status."""
        self.thirst = 1
