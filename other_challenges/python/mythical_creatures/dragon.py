"""Dragon object from Turings Mythical Creatures."""


class Dragon():
    """Methods for dragon object."""

    def __init__(self, name, color, rider):
        """Create a dragon object with a name."""
        self.name = name
        self.color = color
        self.rider = rider
        self.eat_count = 0

    def get_name(self) -> str:
        """Getter method for returning dragon's name."""
        return self.name

    def get_color(self) -> str:
        """Getter method for returning dragon's color."""
        return self.color

    def get_rider(self) -> str:
        """Getter method for returning dragon's rider name."""
        return self.rider

    def is_hungry(self) -> bool:
        """Return if dragon is hungry or not."""
        if self.eat_count <= 3:
            return True
        else:
            return False

    def eat(self):
        """Add to current eat count."""
        self.eat_count += 1
