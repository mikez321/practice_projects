class Node
  def initialize(num)
    @num = num
  end

  def shout
    fizzbuzz(@num)
  end

  def fizzbuzz(value)
    if (value % 3).zero? && (value % 5).zero?
      "Fizzbuzz"
    elsif (value % 3).zero?
      "Fizz"
    elsif (value % 5).zero?
      "Buzz"
    else
      @num.to_s
    end
  end
end
