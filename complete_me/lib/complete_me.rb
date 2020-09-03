require './lib/node'

class CompleteMe
  attr_reader :root

  def initialize
    @root = Node.new(" ")
  end

  def insert(word, current_node = @root)
    #this is almost right, but I need to be naming the new node 'ab' on
    #round 2 and then removing 'ab' from the next new word that gets passed in
    
    require "pry"; binding.pry
    word = (current_node.name + word).delete(' ')
    split_word = word.split('')
    new_node = Node.new(split_word.first)
    current_node.add(new_node)
    split_word.shift
    new_word = split_word.join
    require "pry"; binding.pry
    insert(new_word, new_node)
  end

  def count
    @nodes.length
  end
end
