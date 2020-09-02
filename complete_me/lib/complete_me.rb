require './lib/node'

class CompleteMe
  attr_reader :root, :nodes

  def initialize
    @root = Node.new(" ")
    @nodes = []
  end

  def insert(word)
    new_node = Node.new(word)
    @nodes << new_node
  end

  def count
    @nodes.length
  end
end
