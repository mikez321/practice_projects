require './lib/btree'
require 'minitest/autorun'
require 'minitest/pride'

class BinarySearchTreeTest < Minitest::Test
  def setup
    @tree = BinarySearchTree.new
  end

  def test_it_exists
    assert_instance_of BinarySearchTree, @tree
  end

  def test_root_nodes_have_a_depth_of_zero
    bill = Node.new(61, "Bill & Ted's Excellent Adventure")

    assert_nil @tree.root

    @tree.root = bill

    assert_equal 0, @tree.depth(bill.rating)
  end

  def test_a_tree_knows_the_depth_of_a_rating
    @tree.insert(61, "Bill & Ted's Excellent Adventure")
    @tree.insert(16, "Johnny English")

    assert_equal 1, @tree.depth(16)
  end

  def test_it_can_set_a_node_to_the_left
    @tree.insert(61, "Bill & Ted's Excellent Adventure")

    john = Node.new(16, "Johnny English")

    @tree.set_node(john, @tree.root)

    assert_equal john, @tree.root.left
  end

  def test_it_can_set_a_node_to_the_right
    @tree.insert(61, "Bill & Ted's Excellent Adventure")

    john = Node.new(90, "Johnny English")

    @tree.set_node(john, @tree.root)

    assert_equal john, @tree.root.right
  end

  def test_it_returns_false_if_a_node_exists
    @tree.insert(61, "Bill & Ted's Excellent Adventure")

    john = Node.new(90, "Johnny English")
    sharks = Node.new(92, "Sharknado 3")

    @tree.set_node(john, @tree.root)

    assert_equal false, @tree.set_node(sharks, @tree.root)
  end

  def test_it_can_move_to_the_next_node
    @tree.insert(61, "Bill & Ted's Excellent Adventure")

    john = Node.new(62, "Johnny English")
    sharks = Node.new(92, "Sharknado 3")
    current_node = @tree.root

    @tree.set_node(john, @tree.root)

    current_node = @tree.next_node(sharks, current_node)

    assert_equal false, current_node == @tree.root
    assert_equal true, current_node == john
  end

  def test_it_can_insert_a_node
    skip
    assert_equal 0, @tree.insert(61, "Bill & Ted's Excellent Adventure")
    assert_equal 1, @tree.insert(16, "Johnny English")
    assert_equal 1, @tree.insert(92, "Sharknado 3")
    assert_equal 2, @tree.insert(50, "Hannibal Buress: Animal Furnace")
  end
end
