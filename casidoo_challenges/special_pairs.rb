# Special pairs challenge from cassidoo email issue #170
require 'minitest/autorun'
require 'minitest/pride'

def special_pairs(nums)
  special_pairs = []
  indexes = (0.. nums.length - 1)

  indexes.each do |ind1|
    indexes.each do |ind2|
      if ind1 < ind2 && nums[ind1] == nums[ind2]
        special_pairs << [ind1, ind2]
      end
    end
  end

  special_pairs.length
end

class SpecialPairsTest < Minitest::Test
  def test_it_returns_a_special_pair
    assert_equal special_pairs([1, 2, 3, 1]), 1
  end

  def test_it_returns_all_special_pairs
    assert_equal special_pairs([1, 2, 3, 1, 1, 3]), 4
  end
end
