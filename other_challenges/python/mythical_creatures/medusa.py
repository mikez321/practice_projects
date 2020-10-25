"""Medusa object from Turing's Mythical Creatures."""
class Medusa(object):
    """Medusa object and methods."""

    def __init__(self, name: str) -> object:
        """Initialize with hidden properties."""
        self._name = name
        self._statues = []

    def get_name(self) -> str:
        """Getter method for name prop."""
        return self._name

    def statue_count(self) -> int:
        """Return the number of statues in the collection."""
        return len(self._statues)

    def stare_at(self, victim):
        """
        Stone the person and add to statue collection.

        :param victim: Person object taken in as arg.  The person taken into
            this method will be added to the medusa's collection of statues
            and its property of being stoned will be set to true.
        :return: No return value is produced from this method.
        :note: A Medusa can only have 3 statues at a time.  The fourth statue
            will set the first one free!
        """
        if len(self._statues) == 3:
            self._statues[0].set_stoned(False)
            self._statues = self._statues[1:]

        victim.stoned = True
        self._statues.append(victim)


class Person(object):
    """Badic person object to interact with Medusa."""

    def __init__(self, name) -> object:
        """Initialize a standard person object with a name."""
        self._name = name
        self._stoned = False

    def get_stoned(self):
        """Getter method for stoned status."""
        return self._stoned

    def set_stoned(self, value):
        """Change the value of _stoned."""
        self._stoned = value

    stoned = property(get_stoned, set_stoned)

    def is_stoned(self):
        """Getter method for stoned status."""
        return self._stoned
