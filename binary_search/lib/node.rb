class Node
  attr_reader :rating, :title

  def initialize(rating, title)
    @rating = rating
    @title = title
  end

  def depth
    0
  end
end
