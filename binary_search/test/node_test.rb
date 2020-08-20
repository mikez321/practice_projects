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
end
