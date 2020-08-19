class Node
  attr_reader :name, :supplies
  attr_accessor :next_node

  def initialize(name, supplies)
    @name = name
    @next_node = nil
    @supplies = supplies
  end

  def tail?
    @next_node.nil? ? true : false
  end
end
