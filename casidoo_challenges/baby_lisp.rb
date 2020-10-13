require 'minitest/autorun'
require 'minitest/pride'

def baby_lisp(command)
  math = {
    'add': :+,
    'subtract': :-,
    'multiply': :*,
    'divide': :/
  }

  singles = command.split

  action = singles.first.delete('()').to_sym
  num1 = singles[1].to_f

  if singles[2][0] == '('
    command = singles[2.. -1].join(' ')
    num2 = baby_lisp(command)
  else
    num2 = singles[2].to_f
  end

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
    assert_equal baby_lisp('(subtract 1 (add 3 2))'), -4.0
  end
end
