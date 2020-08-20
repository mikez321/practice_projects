require './lib/node'

class BinarySearchTree
  attr_accessor :root

  def initialize
    @root = nil
  end

  def insert(rating, title)
    new_node = Node.new(rating, title)
    if @root.nil?
      @root = new_node
    elsif
      @root.leaf?
      set_node(new_node, @root)
    elsif
      current_node = @root
      set_node(new_node, current_node)
    end
    depth(new_node.rating)
  end

  def depth(rating)
    left = depth_l(rating)
    right = depth_r(rating)
    left >= right ? left : right
  end

  def depth_l(rating)
    current_node = @root
    depth = 0
    until current_node.left.nil?
      depth += 1
      current_node = current_node.left
    end
    depth
  end

  def depth_r(rating)
    current_node = @root
    depth = 0
    until current_node.right.nil?
      depth += 1
      current_node = current_node.right
    end
    depth
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
end
