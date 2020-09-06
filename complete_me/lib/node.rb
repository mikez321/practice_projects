class Node
  attr_reader :name, :children
  attr_accessor :parent, :word

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

  def all_words(collected_words = [])
    if word?
      collected_words << name
    else
      children.values.each do |node|
        node.all_words(collected_words)
      end
    end
    collected_words
  end

  def word?
    @word
  end
end
