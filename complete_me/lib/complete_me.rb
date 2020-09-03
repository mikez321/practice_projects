require './lib/node'

class CompleteMe
  attr_reader :root

  def initialize
    @root = Node.new(" ")
    @word_count = 0
  end

  def insert(word, current_node = @root)
    if word == ""
      @word_count += 1
      "added new word #{current_node.name}"
    else
      split_word = word.split('')
      new_name = (current_node.name + split_word.shift).delete(' ')
      new_node = Node.new(new_name)
      current_node.add(new_node)
      new_word = split_word.join
      insert(new_word, new_node)
    end
  end

  def count
    @word_count
  end
end
