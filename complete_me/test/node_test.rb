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
end
