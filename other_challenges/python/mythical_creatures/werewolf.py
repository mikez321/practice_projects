"""Werewolf object from Turing's Mythical Creatures."""


class Werewolf:
    """Werewolf object."""

    def __init__(self):
        """Initialize Werewolf object with properties."""
        self.set_defaults()

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

    @property
    def human(self):
        """Return human property."""
        return self._human

    @human.setter
    def human(self, value):
        self._human = value

    @property
    def hungry(self):
        """Getter method for hungry attribute."""
        return self._hungry

    @hungry.setter
    def hungry(self, value):
        self._hungry = value

    def set_defaults(self):
        """Set default values when werewolf is created."""
        self._human = True
        self._hungry = False

    def change(self):
        """Toggle human attribute."""
        self.human = not self.human
        self.hungry = not self.hungry
