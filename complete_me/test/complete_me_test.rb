require './lib/complete_me'
require 'minitest/autorun'
require 'minitest/pride'

class CompleteMeTest < Minitest::Test
  def setup
    @completion = CompleteMe.new
  end

  def test_it_exists
    assert_instance_of CompleteMe, @completion
  end

  def test_it_starts_with_a_blank_root_node
    assert_instance_of Node, @completion.root
  end

  def test_it_can_add_a_one_letter_word
    assert_equal 'added new word a', @completion.insert('a')
  end

  def test_it_can_add_two_letter_words
    assert_equal 'added new word ab', @completion.insert('ab')
  end

  def test_it_knows_how_many_words_it_has
    @completion.insert('a')

    assert_equal 1, @completion.count

    @completion.insert('bee')

    assert_equal 2, @completion.count
  end

  # def test_it_can_add_words
  #   @completion.insert('pizza')
  #
  #   assert_equal 1, @completion.count
  # end
  #
  # def test_it_can_suggest_completions
  #   @completion.insert('pizza')
  #
  #   expected = ['pizza']
  #
  #   assert_equal expected, @completion.suggest('piz')
  # end
end
