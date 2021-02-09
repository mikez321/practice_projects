require 'minitest/autorun'
require 'minitest/pride'

class Number
  attr_reader :value

  def initialize(value)
    @value = value
  end
end

class ProductList
  attr_reader :list

  def initialize
    @list = []
  end

  def add_to_list(num)
    @list << num
  end

  def product(quantity)
    to_multiply = @list.reverse[0, quantity]
    to_multiply.reduce(1) { |result, num| result *= num.value }
  end
end

class ProductListTest < Minitest::Test
  def test_numbers
    num1 = Number.new(1)
    num2 = Number.new(2)

    assert_equal(num1.class, Number)

    assert_equal(num1.value, 1)
    assert_equal(num2.value, 2)
  end

  def test_productlist
    pl = ProductList.new

    assert_equal(pl.class, ProductList)
    assert_equal(pl.list, [])

    num1 = Number.new(1)
    num2 = Number.new(2)

    pl.add_to_list(num1)
    assert_equal(pl.list, [num1])
    pl.add_to_list(num2)
    assert_equal(pl.list, [num1, num2])
  end

  def test_product_function
    pl = ProductList.new
    n = 1
    5.times do
      new = Number.new(n)
      pl.add_to_list(new)
      n += 1
    end

    assert_equal(pl.product(1), 5)
    assert_equal(pl.product(2), 20)
  end
end
