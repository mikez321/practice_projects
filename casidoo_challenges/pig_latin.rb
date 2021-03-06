require 'minitest/autorun'
require 'minitest/pride'

# Write a function that converts a sentence into pig latin

def pig_latinize(string)
  latinize = string[0] + 'ay'
  string.reverse.chop.reverse + latinize
end

def collect_punctuation(word)
  punctuation = []
  until !word[-1].special_character?
    punctuation << word[-1]
    word = word[0..-2]
  end
  {'word' => word, 'punctuation' => punctuation.join('')}
end

def translate(phrase)
  phrase = phrase.split(' ')
  phrase.map do |word|
    if word.upper_case? && word[-1].special_character?
      punctuation = collect_punctuation(word)['punctuation']
      word = collect_punctuation(word)['word']
      pig_latinize(word.downcase).capitalize + punctuation
    elsif word.upper_case?
      pig_latinize(word.downcase).capitalize
    elsif word[-1].special_character?
      punctuation = collect_punctuation(word)['punctuation']
      word = collect_punctuation(word)['word']
      pig_latinize(word) + punctuation
    elsif word.number?
      word
    else
      pig_latinize(word)
    end
  end.join(' ')
end

class String
  def number?
    match(/\d/) ? true : false
  end

  def special_character?
    match(/\W/) ? true : false
  end

  def upper_case?
    match(/[A-Z]/) ? true : false
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

  def test_it_can_identify_special_characters
    characters = ['.', '!', '$', '(']

    characters.each do |character|
      assert_equal true, character.special_character?
    end

    not_special = ['a', '1', 'Z']

    not_special.each do |character|
      assert_equal false, character.special_character?
    end
  end

  def test_it_knows_if_a_word_is_capitalized
    assert_equal true, 'Mike'.upper_case?
    assert_equal false, 'lower'.upper_case?
  end

  def test_it_will_fix_capitalization_errors_it_creates
    assert_equal 'Ikemay', translate('Mike')
  end

  def test_it_can_handle_punctuation
    assert_equal 'igspay!', translate('pigs!')
  end

  def test_it_can_collect_mulitple_punctuations
    word = 'test!!!'

    assert_equal 'test', collect_punctuation(word)['word']
    assert_equal '!!!', collect_punctuation(word)['punctuation']
  end

  def test_it_can_translate_whole_sentences_including_numbers_and_punctuation
    phrase = "I would like 13 donuts please... A Baker's Dozen!"
    expected = "Iay ouldway ikelay 13 onutsday leasepay... Aay Aker'sbay Ozenday!"

    assert_equal expected, translate(phrase)
  end
end
