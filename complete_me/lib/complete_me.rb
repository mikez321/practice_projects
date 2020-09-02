require './lib/node'

class CompleteMe
  attr_reader :root
  
  def initialize
    @root = Node.new(" ")
  end

  def insert(name)
    Node.new(name)
  end

  def count

  end
end
