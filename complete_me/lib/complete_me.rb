require './lib/node'

class CompleteMe
  attr_reader :root

  def initialize
    @root = Node.new(" ")
    @leaves = []
  end

  def insert(name)
    new_node = Node.new(name)
    @root.child = new_node
  end

  def count
    if @root.child && @root.child.leaf?
      @leaves << @root.child.leaf?
      @leaves.count
    else
      0
    end
  end
end
