"""Medusa object from Turing's Mythical Creatures."""
class Medusa(object):
    """Medusa object and methods."""

    def __init__(self, name):
        """Initialize with hidden properties."""
        self._name = name

    def get_name(self):
        """Getter method for name prop."""
        return self.name
