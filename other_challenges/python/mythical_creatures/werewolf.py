"""Werewolf object from Turing's Mythical Creatures."""


class Werewolf:
    """Werewolf object."""

    def __init__(self):
        """Initialize Werewolf object with name and location as properties."""
        self.name = None
        self.location = None

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
