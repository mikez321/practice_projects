require './lib/complete_me'
require 'minitest/autorun'
require 'minitest/pride'

class CompleteMeTest < Minitest::Test
  def setup
    @completion = CompleteMe.new
    @dictionary = File.read('/usr/share/dict/words')
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

  def test_it_can_add_a_new_child_to_an_existing_tree
    @completion.insert('a')
    @completion.insert('bee')

    root = @completion.root

    assert_equal 2, root.children.length

    b = root.children['b']

    assert_instance_of Node, b
    assert_equal 'b', b.name
    assert_equal 1, b.children.length
    assert_equal ['be'], b.children.keys

    @completion.insert('bae')

    assert_equal 3, @completion.count

    assert_equal 2, b.children.length
    assert_equal ['be', 'ba'], b.children.keys

    be = b.children['be']
    ba = b.children['ba']

    assert_equal 'bee', be.children['bee'].name
    assert_equal 'bae', ba.children['bae'].name
  end

  def test_it_can_add_words
    @completion.insert('pizza')

    assert_equal 1, @completion.count
  end

  def test_it_can_suggest_completions
    @completion.insert('pizza')

    expected = ['pizza']

    assert_equal expected, @completion.suggest('piz')
  end

  def test_it_can_load_a_collection_of_words
    @completion.populate(@dictionary)

    assert_equal 235886, @completion.count
  end

  # def test_it_can_suggest_multiple_words
  #   words = [
  #     'eggplant',
  #     'egg',
  #     'elephant',
  #     'escape',
  #     'ever',
  #     'even',
  #     'evergreen',
  #     'eve',
  #     'fond',
  #     'found',
  #     'fern',
  #     'fan'
  #   ]
  #
  #   words = words.join("\n")
  #
  #   @completion.populate(words)
  # end
end
