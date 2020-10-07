require 'minitest/autorun'
require 'minitest/pride'

def nearest_value(numbers, target)
  numbers = numbers.sort
  
  result = numbers.map { |num| (target - num).abs }

  min_index = result.index(result.min)

  numbers[min_index]
end

class NearestTest < Minitest::Test

  def test_it_knows_the_nearest_number
    assert_equal 10, nearest_value([4, 7, 10, 11, 12, 17], 9)
  end

  def test_it_picks_the_smaller_of_two_equally_near_numbers
    assert_equal 8, nearest_value([4, 8, 10, 11, 12, 17], 9)
  end

  def test_it_picks_the_number_if_the_target_is_in_the_array
    assert_equal 9, nearest_value([4, 9, 10, 11, 12, 17], 9)
  end

  def test_the_numbers_can_be_in_any_order
    assert_equal 8, nearest_value([11, 17, 10, 4, 12, 7, 11, 8], 9)
  end

end
