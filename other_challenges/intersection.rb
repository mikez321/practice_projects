require 'minitest/autorun'
require 'minitest/pride'

def find_intersection(strArr)
  all = strArr.first.split + strArr.last.split
  all = all.map { |item| item.delete(',')}

  all.map do |item|
    all.delete(item) if all.count(item) == 1
  end

  all.length.zero? ? false : all.uniq.join(',')
end

class FindIntersectionTest < Minitest::Test
  def test_it_finds_the_numbers_in_both_strings
    assert_equal find_intersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]), '1,4,13'
  end
end
