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
    until node.rating == current_node.rating
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

  def include?(rating)
    rating_node = Node.new(rating, "This node is like a little hunter!")
    current_node = @root
    until next_node(rating_node, current_node).nil?
      return true if rating_node.rating == current_node.rating

      current_node = next_node(rating_node, current_node)
    end
    false
  end

  def depth_of(rating)
    rating_node = Node.new(rating, "This node is like a little traveler!")
    depth(rating_node)
  end

  def max
    max_node_of(@root).info
  end

  def min
    min_node_of(@root).info
  end

  def max_node_of(current_node)
    until current_node.right.nil?
      current_node = current_node.right
    end
    current_node
  end

  def min_node_of(current_node)
    until current_node.left.nil?
      current_node = current_node.left
    end
    current_node
  end

  def sort
    movies = []
    min_node = min_node_of(@root)
    movies << min_node.info
    finder_node = Node.new(min_node.rating, 'This node finds other nodes')
    next_node = next_node(finder_node, @root)
    movies << next_node.info
    require "pry"; binding.pry
    movies
  end

end
