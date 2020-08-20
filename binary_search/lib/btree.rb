require './lib/node'

class BinarySearchTree
  attr_accessor :root

  def initialize
    @root = nil
  end

  def set_node(new_node, current_node)
    if new_node.rating > current_node.rating && current_node.right.nil?
      current_node.right = new_node
    elsif
      new_node.rating < current_node.rating && current_node.left.nil?
      current_node.left = new_node
    else
      false
    end
  end

  def next_node(new_node, current_node)
    if new_node.rating > current_node.rating
      current_node = current_node.right
    elsif
      new_node.rating < current_node.rating
      current_node = current_node.left
    end
    current_node
  end

  def depth(node)
    current_node = @root
    depth = 0
    until node == current_node
      depth += 1
      current_node = next_node(node, current_node)
    end
    depth
  end

  def insert(rating, title)
    new_node = Node.new(rating, title)
    if @root.nil?
      @root = new_node
    else
      current_node = @root
      until next_node(new_node, current_node).nil?
        current_node = next_node(new_node, current_node)
      end
      set_node(new_node, current_node)
    end
    depth(new_node)
  end
end
