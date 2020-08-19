require './lib/node'
require 'minitest/autorun'
require 'minitest/pride'

class NodeTest < Minitest::Test
  def test_it_exists
    node = Node.new("Williams", {"Food": 100})

    assert_instance_of Node, node
  end

  def test_it_has_attributes
    node = Node.new("Williams", {"Food": 100})

    assert_equal "Williams", node.name
    assert_nil node.next_node
  end

  def test_it_can_be_a_tail
    node1 = Node.new("Williams", {"Oxen": 3})
    node2 = Node.new("Young", {"Food": 120})
    node3 = Node.new("Taylor", {"Ammo": 100})

    node1.next_node = node2
    node2.next_node = node3

    assert_equal false, node1.tail?
    assert_equal false, node2.tail?
    assert_equal true, node3.tail?
  end

  def test_it_can_have_supplies
    node1 = Node.new("Williams", {"Food": 100})
    node2 = Node.new("Young", {"Oxen": 5})

    expected1 = {"Food": 100}
    expected2 = {"Oxen": 5}

    assert_equal expected1, node1.supplies
    assert_equal expected2, node2.supplies
    assert_equal false, node1.supplies == node2.supplies
  end
end
