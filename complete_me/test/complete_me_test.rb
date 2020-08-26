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

  def test_it_can_add_words
    @completion.insert('pizza')

    assert_equal 1, @completion.count
  end

  def test_it_can_suggest_completions
    expected = ['pizza']

    assert_equal expected, completion.suggest('piz')
  end
end
