"""Werewolf object from Turing's Mythical Creatures."""


class Werewolf:
    """Werewolf object."""

    def __init__(self, name, location):
        """Initialize Werewolf object with properties."""
        self._name = name
        self._location = location
        self._human = True
        self._hungry = False

    def get_name(self): return self._name

    def set_name(self, name): self._name = name

    def get_location(self): return self._location

    def set_location(self, location): self._location = location

    def get_human(self): return self._human

    def get_hungry(self): return self._hungry

    name = property(get_name, set_name)
    location = property(get_location, set_location)
    human = property(get_human)
    hungry = property(get_hungry)

    def change(self):
        """Toggle human attribute."""
        self._human = not self._human
        self._hungry = not self._hungry
