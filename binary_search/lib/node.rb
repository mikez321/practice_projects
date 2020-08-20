class Node
  attr_reader :rating, :title
  attr_accessor :left, :right

  def initialize(rating, title)
    @rating = rating
    @title = title
    @left = nil
    @right = nil
  end

  def leaf?
    left.nil? && right.nil? ? true : false
  end

  def info
    { @title => @rating }
  end
end
