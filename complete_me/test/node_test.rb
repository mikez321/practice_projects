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

    assert_equal [node2], @node.children.values
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

    assert_equal expected, @node.children.values
  end

  def test_it_knows_its_parent_node
    node2 = Node.new('brew')

    @node.add(node2)

    assert_equal @node, node2.parent
  end

  def test_it_knows_all_the_words_under_it
    node1 = Node.new(' ')
    node2 = Node.new('a')
    node3 = Node.new('am')
    node4 = Node.new('at')

    node3.word = true
    node4.word = true

    node1.add(node2)
    node2.add(node3)
    node2.add(node4)

    assert_equal ['am', 'at'], node1.all_words
  end

  def test_it_knows_if_it_is_a_complete_word
    node1 = Node.new('th')
    node2 = Node.new('the')

    node2.word = true

    assert_equal false, node1.word?
    assert_equal true, node2.word?
  end
end
