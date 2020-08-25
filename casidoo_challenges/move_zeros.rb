# Given an array of random integers, move all the zeros in the array to the end
# of the array. Try to keep this in O(n) time (or better)!

#Example:

# moveZeros([1, 2, 0, 1, 0, 0, 3, 6])
# [1, 2, 1, 3, 6, 0, 0, 0]

require 'minitest/autorun'
require 'minitest/pride'

def move_zeros(array)
  zeros = []
  array.each do |num|
    num.zero? ? zeros << num : next
  end.delete(0)
  array + zeros
end

class MoveZerosTest < Minitest::Test
  def test_it_can_move_zeros_to_the_end
    array = [1, 2, 0, 1, 0, 0, 3, 6]
    expected = [1, 2, 1, 3, 6, 0, 0, 0]

    assert_equal expected, move_zeros(array)
  end
end
