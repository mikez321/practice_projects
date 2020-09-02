class Node
  attr_reader :name, :child

  def initialize(name)
    @name = name
    @child
  end

  def child=(node)
    @child = node
  end
end
