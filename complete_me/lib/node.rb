class Node
  attr_reader :name, :child

  def initialize(name)
    @name = name
    @child = nil
  end

  def child=(node)
    @child = node
  end

  def leaf?
    @child.nil? ? true : false
  end
end
