class Node
  attr_reader :left, :right, :title
  attr_accessor :parent, :rating

  def initialize(rating, title)
    @rating = rating
    @title = title
    @left = nil
    @right = nil
    @parent = nil
  end

  def leaf?
    left.nil? && right.nil? ? true : false
  end

  def info
    { @title => @rating }
  end

  def left=(node)
    node.parent = self
    @left = node
  end

  def right=(node)
    node.parent = self
    @right = node
  end

  def abandon
    @left = nil
  end
end
