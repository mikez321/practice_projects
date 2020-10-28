"""Testing for nodes."""
from node import Node


def test_it_exists():
    """Create a node."""
    node = Node(1)
    assert type(node) == Node


def test_born_alone():
    """New nodes have no nodes to their left or right."""
    node = Node(4)
    assert node.left is None
    assert node.right is None
