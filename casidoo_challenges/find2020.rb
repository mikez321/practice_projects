require 'minitest/autorun'
require 'minitest/pride'

def find2020(number, index = 0, result = -1)
  if number.length < 4
    result
  else
    first_four = number[0, 4]
    if first_four == '2020'
      result = index
    else
      number = number[1, number.length - 1]
      index += 1
      find2020(number, index, result)
    end
  end
end

class FindTwentyTwentyTest < Minitest::Test
  def test_it_works
    assert_equal(1, 1)
  end

  def test_no_2020_returns_minus_one
    assert_equal(find2020('1'), -1)
    assert_equal(find2020('222'), -1)
    assert_equal(find2020('22200'), -1)
  end

  def test_it_can_find_a_2020
    assert_equal(find2020('2002022020002'), 6)
    assert_equal(find2020('00020002002020'), 10)
    assert_equal(find2020('20200'), 0)
  end
end
