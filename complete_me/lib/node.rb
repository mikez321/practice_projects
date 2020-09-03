class Node
  attr_reader :name, :children
  attr_accessor :parent

  def initialize(name)
    @name = name
    @children = []
    @parent = nil
  end

  def add(node)
    node.parent = self
    @children << node
  end

  def leaf?
    @children.length.zero? ? true : false
  end
end
