require 'minitest/autorun'
require 'minitest/pride'

def find2020(number)
  -1 if number.length < 4
end

class FindTwentyTwentyTest < Minitest::Test
  def test_it_works
    assert_equal(1, 1)
  end

  def test_no_2020_returns_minus_one
    assert_equal(find2020([1]), -1)
  end
end
