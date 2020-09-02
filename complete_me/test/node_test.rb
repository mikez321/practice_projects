require './lib/node'
require 'minitest/autorun'
require 'minitest/pride'

class NodeTest < Minitest::Test
  def setup
    @node = Node.new('ale')
  end

  def test_it_exists
    assert_instance_of Node, @node
  end

  def test_it_can_have_a_child_node
    node2 = Node.new('brew')

    @node.child = node2

    assert_equal node2, @node.child
  end

  def test_it_is_leaf_if_it_has_no_children
    node2 = Node.new('brew')

    @node.child = node2

    assert_equal false, @node.leaf?
    assert_equal true, node2.leaf?
  end
end
