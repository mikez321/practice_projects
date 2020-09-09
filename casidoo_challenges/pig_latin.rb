require 'minitest/autorun'
require 'minitest/pride'

# Write a function that converts a sentence into pig latin

def pig_latinize(string)
  latinize = string[0] + 'ay'
  string.reverse.chop.reverse + latinize
end

class PigLatinTest < Minitest::Test

  def test_it_can_turn_a_word_into_pig_latin
    assert_equal 'igpay', pig_latinize('pig')
    assert_equal 'atinlay', pig_latinize('latin')
  end

  def test_it_can_translate_multiple_words
    assert_equal 'igpay atinlay', translate('pig latin')
  end
end
