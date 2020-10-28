"""Node class for making a standard linked list."""


class Node(object):
    """This is a single node to be added to a linked list."""

    def __init__(self, number):
        """Initialize a new object with a number value."""
        self.number = number
        self.right = None
        self.left = None
