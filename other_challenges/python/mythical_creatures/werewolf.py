"""Werewolf object from Turing's Mythical Creatures."""


class Werewolf:
    """Werewolf object."""

    def __init__(self):
        """Initialize Werewolf object with name and location as properties."""
        self.name = None
        self.location = None
        self.human = True

    @property
    def name(self):
        """Getter method to return name."""
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def location(self):
        """Getter method to return location."""
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    def is_human(self):
        """Return attribute of human or not."""
        return self.human

    def change(self):
        """Toggle human attribute."""
        self.human = not self.human
