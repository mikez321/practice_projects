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

    @node.add(node2)

    assert_equal [node2], @node.children
  end

  def test_it_is_leaf_if_it_has_no_children
    node2 = Node.new('brew')

    @node.add(node2)

    assert_equal false, @node.leaf?
    assert_equal true, node2.leaf?
  end

  def test_it_can_have_more_than_one_child
    node2 = Node.new('brew')
    node3 = Node.new('chill')
    node4 = Node.new('carbonate')

    @node.add(node2)
    @node.add(node3)
    @node.add(node4)

    expected = [node2, node3, node4]

    assert_equal expected, @node.children
  end
end
