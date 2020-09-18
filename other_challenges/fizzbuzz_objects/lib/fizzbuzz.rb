require './lib/node'

class Fizzbuzz
  def self.go(low, high)
    range = (low..high).to_a

    range.map { |num| Node.new(num).shout }
  end
end
