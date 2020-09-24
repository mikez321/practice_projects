require 'minitest/autorun'
require 'minitest/pride'


# Given an array of increasing integers, find the length of the longest
# fibonacci-like subsequence of the array. If one does not exist, return 0

# fibonacciLike([1,3,7,11,12,14,18])
# 3 // these sequences: [1,11,12], [3,11,14] or [7,11,18]

def fibonacci_like(numbers, longest = [])
  return longest.length if numbers.length.zero?
  start = numbers.shift
  numbers.each do |num|
    if numbers.include?(next_number(start, num))
      sequence = [start, num, next_number(start, num)]
      until !numbers.include?(next_number sequence[-2], sequence[-1])
        sequence << next_number(sequence[-2], sequence[-1])
      end
    end
    longest = sequence  if sequence && sequence.length > longest.length
  end
  fibonacci_like(numbers, longest)
end

def next_number(num1, num2)
  num1 + num2
end

class FibLikeTest < Minitest::Test
  def test_it_can_identify_fib_like_numbers
    assert_equal 3, fibonacci_like([1,3,7,11,12,14,18])
  end

  def test_if_no_fib_like_sequence_it_returns_zero
    assert_equal 0, fibonacci_like([1,3,7,9,11,30])
  end

  def test_it_can_return_the_longest_fib_like_sequence
    assert_equal 6, fibonacci_like([1,3,4,8,11,12,14,15,17,18,20,38,58,96,154])
  end

  def test_it_knows_the_next_fib_like_number
    assert_equal 2, next_number(1, 1)
    assert_equal 3, next_number(1, 2)
    assert_equal 5, next_number(2, 3)
    assert_equal 8, next_number(3, 5)
    assert_equal 13, next_number(5, 8)
  end
end
