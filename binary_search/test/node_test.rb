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
end
