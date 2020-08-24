# Given a string s and a character c, return the number of occurrences of c in s.
# Ex: num_chars('oh heavens', 'h')
# => 2

require 'minitest/autorun'
require 'minitest/pride'

def num_chars(phrase, letter)
  phrase.split('').map do |phrase_letter|
    phrase_letter == letter ? true : nil
  end.compact.length
end


class NumCharsTest < Minitest::Test
  def test_it_can_return_number_of_occurrances_of_a_letter
    assert_equal 8, num_chars('she sells seashells down by the seashore', 's')
  end
end
