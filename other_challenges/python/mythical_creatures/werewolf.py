"""Werewolf object from Turing's Mythical Creatures."""


class Werewolf(object):
    """Werewolf object."""

    def __init__(self, name, location):
        """Initialize Werewolf object with hidden properties."""
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

    def consume(self, prey):
        """Werewolf can consume victims."""
        if self._human is True:
            return "I ain't no savage."
        else:
            self._hungry = not self._hungry
            prey.set_status('dead')
            return 'Nom Nom Nom'


class Victim(object):
    """Victim object to interact with werewolf."""

    def __init__(self):
        """Initialize a new victim object with a status of alive."""
        self._status = 'alive'

    def get_status(self): return self._status

    def set_status(self, status): self._status = status

    status = property(get_status, set_status)
