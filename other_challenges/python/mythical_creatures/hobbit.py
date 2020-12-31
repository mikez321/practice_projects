"""Hobbit mythical creature."""


class Hobbit(object):
    """A hobbit object."""

    def __init__(self, name):
        """Initialize with name and attributes."""
        self.name = name.capitalize()
        self.disposition = "adventurous"
        self.age = 0

    def is_short(self):
        """All hobbits are short."""
        return True

    def celebrate_birthday(self):
        """Increase age by 1 for each birthday."""
        self.age += 1

    def is_adult(self):
        """Return True if its age is more than 32."""
        adult_status = False
        adult_status = True if self.age > 32 else adult_status
        return adult_status

    def is_old(self):
        """Return true if age is greater than 100."""
        old = False
        old = True if self.age > 100 else old
        return old

    def has_ring(self):
        """Return true if hobbit's name is Danielle."""
        return self.name == "Danielle"

    def __str__(self):
        """Magic method."""
        return f"A hobbit object named {self.name}"
