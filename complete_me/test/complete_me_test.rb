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
    @completion.insert('a')

    assert_equal 1, @completion.count
  end

  def test_it_can_add_two_letter_words
    @completion.insert('ab')

    assert_equal 1, @completion.count
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
