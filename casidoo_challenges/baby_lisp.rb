require 'minitest/autorun'
require 'minitest/pride'

def baby_lisp(command)
  action = command.delete('()').split.first
  num1 = command.delete('()').split[-2].to_i
  num2 = command.delete('()').split[-1].to_i

  if action == 'add'
    num1 + num2
  elsif action == 'subtract'
    num1 - num2
  elsif action == 'multiply'
    num1 * num2
  elsif action == 'divide'
    num1.to_f / num2
  else
    "I don't know how to {action}"
  end

end

class BabyLispTest < Minitest::Test
  def test_it_can_add
    assert_equal baby_lisp('(add 3 2)'), 5
  end

  def test_it_can_subtract
    assert_equal baby_lisp('(subtract 3 2)'), 1
  end

  def test_it_can_multiply
    assert_equal baby_lisp('(multiply 3 2)'), 6
  end

  def test_it_can_divide
    assert_equal baby_lisp('(divide 3 2)'), 1.5
  end
end
