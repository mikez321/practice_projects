"""List of nodes."""


class Llist(object):
    """List class to be filled with nodes."""

    def __init__(self):
        """List is not Initialized with anything."""
        self.nodes = None

    def add(self, node):
        """Nodes can be added to a list."""
        if self.nodes is None:
            self.nodes = node

        return f"Added new node with value of {node.number}"
