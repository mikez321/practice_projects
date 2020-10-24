"""Dragon object from Turings Mythical Creatures."""


class Dragon():
    """Methods for dragon object."""

    def __init__(self, name, color, rider):
        """Create a dragon object with a name."""
        self.name = name
        self.color = color
        self.rider = rider

    def get_name(self):
        """Getter method for returning dragon's name."""
        return self.name

    def get_color(self):
        """Getter method for returning dragon's color."""
        return self.color

    def get_rider(self):
        """Getter method for returning dragon's rider name."""
        return self.rider
