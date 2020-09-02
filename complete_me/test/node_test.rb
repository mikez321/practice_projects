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
end
