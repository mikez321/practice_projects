require './lib/btree'
require 'minitest/autorun'
require 'minitest/pride'

class BinarySearchTreeTest < Minitest::Test
  def setup
    @tree = BinarySearchTree.new
    @tree.insert(61, "Bill & Ted's Excellent Adventure")
    @tree.insert(16, "Johnny English")
    @tree.insert(92, "Sharknado 3")
    @tree.insert(50, "Hannibal Buress: Animal Furnace")
  end

  # The following tests are part of the initial setup and do not use the
  # setup method.

  def test_it_exists
    initial_tree = BinarySearchTree.new
    assert_instance_of BinarySearchTree, initial_tree
  end

  def test_root_nodes_have_a_depth_of_zero
    initial_tree = BinarySearchTree.new

    bill = Node.new(61, "Bill & Ted's Excellent Adventure")

    assert_nil initial_tree.root

    initial_tree.root = bill

    assert_equal 0, initial_tree.depth(bill)
  end

  def test_it_can_set_a_node_to_the_left
    initial_tree = BinarySearchTree.new

    initial_tree.insert(61, "Bill & Ted's Excellent Adventure")

    john = Node.new(16, "Johnny English")

    initial_tree.set_node(john, initial_tree.root)

    assert_equal john, initial_tree.root.left
  end

  def test_it_can_set_a_node_to_the_right
    initial_tree = BinarySearchTree.new

    initial_tree.insert(61, "Bill & Ted's Excellent Adventure")

    john = Node.new(90, "Johnny English")

    initial_tree.set_node(john, initial_tree.root)

    assert_equal john, initial_tree.root.right
  end

  def test_it_returns_false_if_a_node_cannot_be_placed
    initial_tree = BinarySearchTree.new

    initial_tree.insert(61, "Bill & Ted's Excellent Adventure")

    john = Node.new(90, "Johnny English")
    sharks = Node.new(92, "Sharknado 3")

    initial_tree.set_node(john, initial_tree.root)

    assert_equal false, initial_tree.set_node(sharks, initial_tree.root)
  end

  def test_it_can_move_to_the_next_node
    initial_tree = BinarySearchTree.new

    initial_tree.insert(61, "Bill & Ted's Excellent Adventure")

    john = Node.new(62, "Johnny English")
    sharks = Node.new(92, "Sharknado 3")
    current_node = initial_tree.root

    initial_tree.set_node(john, initial_tree.root)

    current_node = initial_tree.next_node(sharks, current_node)

    assert_equal false, current_node == initial_tree.root
    assert_equal true, current_node == john
  end

  def test_a_initial_tree_knows_the_depth_of_a_node
    initial_tree = BinarySearchTree.new

    initial_tree.insert(61, "Bill & Ted's Excellent Adventure")
    john = Node.new(16, "Johnny English")

    initial_tree.set_node(john, initial_tree.root)

    assert_equal 1, initial_tree.depth(john)
  end

  # Starting here all tests will use the setup and instance variables
  # At this point it is assumed we're using a tree with 4 nodes

  def test_it_knows_if_it_includes_a_rating
    assert_equal true, @tree.include?(16)
    assert_equal true, @tree.include?(92)
    assert_equal true, @tree.include?(50)
    assert_equal true, @tree.include?(61)
    assert_equal false, @tree.include?(72)
  end

  def test_it_can_return_the_depth_of_a_rating
    assert_equal 1, @tree.depth_of(92)
    assert_equal 2, @tree.depth_of(50)
  end

  def it_can_return_the_highest_and_lowest_rated_nodes
    assert_instance_of Node, @tree.max_node
    assert_instance_of Node, @tree.min_node

    assert_equal 92, @tree.max_node.rating
    assert_equal 16, @tree.min_node.rating
  end

  def test_it_knows_the_highest_rated_movie_in_the_tree
    expected = {'Sharknado 3' => 92}

    assert_equal expected, @tree.max
  end

  def test_it_knows_the_lowest_rated_movie_in_the_tree
    expected = {'Johnny English' => 16}

    assert_equal expected, @tree.min
  end

  def test_it_can_return_a_sorted_list_of_movies_in_the_tree
    expected = [
      {"Johnny English"=>16},
      {"Hannibal Buress: Animal Furnace"=>50},
      {"Bill & Ted's Excellent Adventure"=>61},
      {"Sharknado 3"=>92}
    ]

    assert_equal expected, @tree.sort
  end

end
