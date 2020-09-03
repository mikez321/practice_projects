class Node
  attr_reader :name, :children

  def initialize(name)
    @name = name
    @children = []
  end

  def add(node)
    @children << node
  end

  def leaf?
    @children.length.zero? ? true : false
  end
end
