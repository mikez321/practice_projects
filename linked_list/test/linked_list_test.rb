require './lib/linked_list'
require 'minitest/autorun'
require 'minitest/pride'

class LinkedListTest < Minitest::Test
  def test_it_exists
    list = LinkedList.new

    assert_instance_of LinkedList, list
  end

  def test_it_has_no_head_at_first
    list = LinkedList.new

    assert_nil list.head
  end

  def test_it_can_add_a_node
    list = LinkedList.new

    list.append("Williams", {"Food": 100})

    assert_nil list.head.next_node
    assert_equal 1, list.count
  end

  def test_it_can_print_out_a_name
    list = LinkedList.new
    list.append("Williams", {"Food": 100})

    assert_equal "The Williams family!", list.to_string
  end

  def test_it_can_add_multiple_nodes
    list = LinkedList.new

    list.append("Williams", {"Food": 100})

    assert_instance_of Node, list.append("Taylor", {"Oxen": 3})
    assert_equal "Taylor", list.head.next_node.name
    assert_equal 2, list.count
  end

  def test_it_can_print_out_multiple_names
    list = LinkedList.new
    list.append("Williams", {"Food": 100})
    list.append("Taylor", {"Oxen": 3})

    assert_equal "The Williams family, followed by the Taylor family!", list.to_string
  end

  def test_it_can_introduce_different_types_of_nodes
    list = LinkedList.new

    list.append("Williams", "Food": 100)

    assert_equal "The Williams family!", list.introducer(list.head)

    node_t = Node.new("Taylor", {"Oxen": 3})
    node_w = Node.new("West", {"Wagon Axles": 2})

    node_t.next_node = node_w

    assert_equal false, list.head == node_t
    assert_equal false, node_t.tail?
    assert_equal true, node_w.tail?

    assert_equal " followed by the #{node_t.name} family,", list.introducer(node_t)
    assert_equal " followed by the #{node_w.name} family!", list.introducer(node_w)
  end

  def test_it_can_add_a_node_to_the_beginning_of_a_list
    list = LinkedList.new
    list.append("Williams", {"Food": 100})

    assert_equal "The Williams family!", list.to_string

    list.append("Taylor", {"Oxen": 3})

    assert_equal "The Williams family, followed by the Taylor family!", list.to_string

    list.prepend("Newport", {"Food": 200})

    assert_equal "The Newport family, followed by the Williams family, followed by the Taylor family!", list.to_string

    assert_equal 3, list.count
  end

  def test_it_can_insert_a_node_into_a_defined_position
    list = LinkedList.new

    list.append("Williams", {"Food": 300})
    list.append("Taylor", {"Oxen": 3})
    list.append("West", {"Boots": 6})

    assert_equal "The Williams family, followed by the Taylor family, followed by the West family!", list.to_string

    list.prepend("Morochovitz", {"Medicine": 30})

    assert_equal "The Morochovitz family, followed by the Williams family, followed by the Taylor family, followed by the West family!", list.to_string

    list.insert(1, "Brown", {"Juice": 100})

    assert_equal "The Morochovitz family, followed by the Brown family, followed by the Williams family, followed by the Taylor family, followed by the West family!", list.to_string
  end

  def test_it_can_find_a_node
    list = LinkedList.new

    list.append("Williams", {"Food": 100})
    list.append("Taylor", {"Food": 100})
    list.append("West", {"Food": 100})
    list.append("Brown", {"Food": 100})
    list.append("Morochovitz", {"Food": 100})
    list.append("Smith", {"Food": 100})
    list.append("Jespen", {"Food": 100})

    assert_equal "West", list.find(2, 1)
    assert_equal "West, Brown, Morochovitz", list.find(2, 3)
    assert_equal true, list.includes?("Brown")
    assert_equal false, list.includes?("Gambino")
  end

  def test_it_can_remove_the_last_node
    list = LinkedList.new

    list.append("Williams", {"Food": 100})
    list.append("Taylor", {"Food": 100})
    list.append("West", {"Food": 100})
    list.append("Smith", {"Food": 100})

    assert_equal "The Smith family has died of dysentery.", list.pop
    assert_equal "The West family has died of dysentery.", list.pop
    assert_equal "The Williams family, followed by the Taylor family!", list.to_string
  end
end
