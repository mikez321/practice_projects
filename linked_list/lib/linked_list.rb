require './lib/node'

class LinkedList
  attr_reader :head, :count

  def initialize
    @head = nil
    @count = 0
  end

  def append(name, supplies)
    if @head.nil?
      @head = Node.new(name, supplies)
    else
      current_node = @head
      until current_node.tail?
        current_node = current_node.next_node
      end
      current_node.next_node = Node.new(name, supplies)
    end
    @count += 1
    @head
  end

  def to_string
    node = @head
    sentence = []
    until node.nil?
      sentence << introducer(node)
      node = node.next_node
    end
    sentence.join
  end

  def introducer(node)
    if node == @head && node.tail?
      "The #{node.name} family!"
    elsif node == @head
      "The #{node.name} family,"
    elsif node.tail?
      " followed by the #{node.name} family!"
    else
      " followed by the #{node.name} family,"
    end
  end

  def prepend(name, supplies)
    prepend_node = Node.new(name, supplies)
    prepend_node.next_node = @head
    @head = prepend_node
    @count += 1
    @head
  end

  def insert(place, name, supplies)
    node = @head
    (place - 1).times do
      node = node.next_node
    end
    inserted_node = Node.new(name, supplies)
    old_next_node = node.next_node
    node.next_node = inserted_node
    inserted_node.next_node = old_next_node
    inserted_node
  end

  def find(place, quantity)
    node = @head
    others = []
    place.times do
      node = node.next_node
    end
    quantity.times do
      others << node.name
      node = node.next_node
    end
    others.join(", ")
  end

  def includes?(search_name)
    node = @head
    until node.nil?
      return true if node.name == search_name
      node = node.next_node
    end
    false
  end

  def pop
    node = @head
    until node.next_node.tail?
      node = node.next_node
    end
    name = node.next_node.name
    node.next_node = nil
    "The #{name} family has died of dysentery."
  end

end
