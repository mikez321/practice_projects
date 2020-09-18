require './lib/fizzbuzz'
require 'minitest/autorun'
require 'minitest/pride'

class FizzbuzzTest < Minitest::Test
  def test_it_exists
    fb = Fizzbuzz.new
    assert_instance_of Fizzbuzz, fb
  end

  def test_it_will_fizz_buzz
    expected = ['1', '2', 'Fizz', '4', 'Buzz',
                'Fizz', '7', '8', 'Fizz', 'Buzz',
                '11', 'Fizz', '13', '14', 'Fizzbuzz']

    assert_equal expected, Fizzbuzz.go(1, 15)
  end
end
