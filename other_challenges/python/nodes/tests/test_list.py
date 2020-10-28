"""Testing for lists."""
from list import Llist
from node import Node


def test_it_exists():
    """Make sure a new llist is created."""
    llist = Llist()
    assert type(llist) == Llist


def test_a_list_can_have_a_node():
    """A node can be added to a list."""
    llist = Llist()
    node1 = Node(1)
    assert llist.nodes is None
    assert llist.add(node1) == f"Added new node with value of {node1.number}"
    assert llist.nodes == (node1)
