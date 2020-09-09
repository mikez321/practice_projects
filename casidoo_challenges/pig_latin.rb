require 'minitest/autorun'
require 'minitest/pride'

# Write a function that converts a sentence into pig latin

def pig_latinize(string)
  latinize = string[0] + 'ay'
  string.reverse.chop.reverse + latinize
end

def translate(phrase)
  phrase = phrase.split(' ')
  phrase.map do |word|
    word.number? ? word : pig_latinize(word)
  end.join(' ')
end

class String
  def number?
    match(/\d/) ? true : false
  end
end

class PigLatinTest < Minitest::Test

  def test_it_can_turn_a_word_into_pig_latin
    assert_equal 'igpay', pig_latinize('pig')
    assert_equal 'atinlay', pig_latinize('latin')
  end

  def test_it_can_translate_multiple_words
    assert_equal 'igpay atinlay', translate('pig latin')
  end

  def test_it_can_identify_a_number
    assert_equal true, '13'.number?
    assert_equal false, 'pig'.number?
  end

  def test_it_can_translate_whole_sentences_including_numbers_and_punctuation
    phrase = "I would like 13 donuts please... a Baker's Dozen!"
    expected = "Iay ouldway ikelay 13 onutsday leasepay... aya aker'sBay ozenDay!"

    assert_equal expected, translate(phrase)
  end
end
