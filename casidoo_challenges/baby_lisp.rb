require 'minitest/autorun'
require 'minitest/pride'

def baby_lisp(command)
  math = {
    'add': :+,
    'subtract': :-,
    'multiply': :*,
    'divide': :/
  }

  action = command.delete('()').split.first.to_sym
  num1 = command.delete('()').split[-2].to_f
  num2 = command.delete('()').split[-1].to_i

  num1.send(math[action], num2)
end

class BabyLispTest < Minitest::Test
  def test_it_can_add
    assert_equal baby_lisp('(add 3 2)'), 5.0
  end

  def test_it_can_subtract
    assert_equal baby_lisp('(subtract 3 2)'), 1.0
  end

  def test_it_can_multiply
    assert_equal baby_lisp('(multiply 3 2)'), 6.0
  end

  def test_it_can_divide
    assert_equal baby_lisp('(divide 3 2)'), 1.5
  end

  def test_it_can_perform_more_than_one_calculation
    assert_equal baby_lisp('(subtract 1 (add 3 2))'), 5.0
  end
end
