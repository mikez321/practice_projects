class Node
  attr_reader :name, :children
  attr_accessor :parent

  def initialize(name)
    @name = name
    @children = {}
    @parent = nil
    @word = false
  end

  def add(node)
    node.parent = self
    @children[node.name] = node
  end

  def leaf?
    @children.keys.length.zero? ? true : false
  end

  def all_words(leaf_words = [])
    if leaf?
      leaf_words << name
    else
      children.values.each do |node|
        node.all_words(leaf_words)
      end
    end
    leaf_words
  end

  def word?
    @word
  end

  def word
    @word = true
  end
end
