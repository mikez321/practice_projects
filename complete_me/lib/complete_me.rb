require './lib/node'

class CompleteMe
  attr_reader :root

  def initialize
    @root = Node.new(" ")
  end

  def insert(word, current_node = @root)
    if word == ""
      'added'
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
    @nodes.length
  end
end
