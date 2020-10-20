require 'minitest/autorun'
require 'minitest/pride'

def freq(sample_dates, **kwargs)
  result = []

  sample_dates.each do |date|
    month = date.split('/').first
    day = date.split('/')[1]
    year = date.split('/').last

    if kwargs[:match_month] == month
      result << date
    elsif kwargs[:match_day] == day
      result << date
    elsif kwargs[:match_year] == year
      result << date
    end
  end

  result.length
end

class DateTest < Minitest::Test
  def setup
    @dates = [
        "11/14/2019",
        "12/26/2019",
        "1/1/2020",
        "1/19/2020",
        "2/11/2020",
        "2/15/2020",
        "3/11/2020",
        "4/5/2020",
        "4/11/2020",
        "4/14/2020",
        "4/26/2020",
    ]
  end

  def test_it_can_return_number_of_matching_months
    assert_equal freq(@dates, match_month:'3'), 1
  end

  def test_it_can_return_number_of_matching_days
    assert_equal freq(@dates, match_day:'11'), 3
  end

  def test_it_can_return_number_of_matching_years
    assert_equal freq(@dates, match_year:'2019'), 2
  end
end
