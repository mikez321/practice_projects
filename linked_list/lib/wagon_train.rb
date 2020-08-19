require './lib/linked_list'

class WagonTrain
  attr_reader :list

  def initialize
    @list = LinkedList.new
  end

  def append(name, supplies)
    @list.append(name, supplies)
  end

  def count
    @list.count
  end

  def supplies
    node = @list.head
    supplies = {}
    until node.nil?
      node.supplies.each do |name, quantity|
        if supplies[name]
          supplies[name] += quantity
        else
          supplies[name] = quantity
        end
      end
      node = node.next_node
    end
    supplies
  end
end
