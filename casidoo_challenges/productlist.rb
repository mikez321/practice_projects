require 'minitest/autorun'
require 'minitest/pride'

class Number
  attr_reader :value

  def initialize(value)
    @value = value
  end
end

class ProductListTest < Minitest::Test
  def test_numbers
    num1 = Number.new(1)
    num2 = Number.new(2)

    assert_equal(num1.value, 1)
    assert_equal(num2.value, 2)
  end
end
