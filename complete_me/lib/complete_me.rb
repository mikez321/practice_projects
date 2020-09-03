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
    elsif
      current_node.children.keys.include?(word[0])
      split_word = word.split('')
      current_node = current_node.children[split_word[0]]
      split_word.shift
      new_word = split_word.join
      insert(new_word, current_node)
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
