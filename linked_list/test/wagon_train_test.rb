require "./lib/wagon_train"
require "minitest/autorun"
require "minitest/pride"

class WagonTrainTest < Minitest::Test
  def test_it_exists
    wt = WagonTrain.new

    assert_instance_of WagonTrain, wt
    assert_instance_of LinkedList, wt.list
  end

  def test_it_can_append_to_its_linked_list
    wt = WagonTrain.new

    assert_nil wt.list.head

    wt.append("Williams", {"Food": 100})

    assert_instance_of Node, wt.list.head
    assert_equal "Williams", wt.list.head.name

    wt.append("Taylor", {"Oxen": 3})

    assert_equal 2, wt.count
  end

  def test_it_can_have_supplies
    wt = WagonTrain.new

    wt.append("Williams", {"Food": 100})
    wt.append("Taylor", {"Food": 200, "Wagon Wheels": 3})
    wt.append("West", {"Food": 100, "Ammo": 500})

    assert_equal 3, wt.count

    expected = {
      "Food": 400,
      "Wagon Wheels": 3,
      "Ammo": 500
    }

    assert_equal expected, wt.supplies
  end
end
