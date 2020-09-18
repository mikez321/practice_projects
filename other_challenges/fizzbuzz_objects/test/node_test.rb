require './lib/node'
require 'minitest/autorun'
require 'minitest/pride'

class NodeTest < Minitest::Test
  def setup
    @node1 = Node.new(1)
    @node3 = Node.new(3)
    @node5 = Node.new(5)
    @node15 = Node.new(15)
  end

  def test_it_exists
    assert_instance_of Node, @node1
  end

  def test_it_can_shout
    assert_equal "1", @node1.shout
  end

  def test_it_can_shout_if_it_fizzes_or_buzzes
    assert_equal "Fizz", @node3.shout
    assert_equal "Buzz", @node5.shout
    assert_equal "Fizzbuzz", @node15.shout
  end
end
