require 'minitest/autorun'
require 'minitest/pride'


# Given an array of increasing integers, find the length of the longest
# fibonacci-like subsequence of the array. If one does not exist, return 0

# fibonacciLike([1,3,7,11,12,14,18])
# 3 // these sequences: [1,11,12], [3,11,14] or [7,11,18]

def fibonacci_like(numbers, sequence = [])
  number = numbers.shift
  numbers.each do |fib|
    if numbers.include?(number + fib)
      return [number, fib, (number + fib)]
    else
      0
    end
  end
end

class FibLikeTest < Minitest::Test
  def test_it_can_identify_fib_like_numbers
    assert_equal [1,11,12], fibonacci_like([1,3,7,11,12,14,18])
  end
end
