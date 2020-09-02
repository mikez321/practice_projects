require 'minitest/autorun'
require 'minitest/pride'

# Given a string find its first uppercase letter
#
# Input : geeksforgeeKs
# Output : K

def uppercase(word)
  word = word.split("")
  if word.first.capitalize == word.first
    return word.first
  else
    word.shift
    uppercase(word.join(''))
  end
end

class UpperCaseTest < Minitest::Test
  def test_it_can_find_the_first_upper_case_letter
    assert_equal 'K', uppercase('geeksforgeeKs')
  end
end
