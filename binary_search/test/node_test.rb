require './lib/node'
require 'minitest/autorun'
require 'minitest/pride'

class NodeTest < Minitest::Test
  def setup
    @node = Node.new(90, "Gentleman Broncos")
  end

  def test_it_exists
    assert_instance_of Node, @node
  end

  def test_it_has_a_score_and_movie_title
    assert_instance_of Integer, @node.rating
    assert_equal "Gentleman Broncos", @node.title
  end

  def test_it_starts_with_no_left_or_right_nodes
    assert_nil @node.left
    assert_nil @node.right
  end

  def test_it_is_a_leaf_if_it_has_no_connected_nodes
    node1 = Node.new(90, "Gentleman Broncos")
    node2 = Node.new(30, "A Detective Calls")
    node3 = Node.new(91, "Sin City")
    node4 = Node.new(95, "The Watchmen")

    node1.left = node2
    node1.right = node3
    node3.right = node4

    assert_equal false, node1.leaf?
    assert_equal true, node2.leaf?
    assert_equal false, node3.leaf?
    assert_equal true, node4.leaf?
  end
end
