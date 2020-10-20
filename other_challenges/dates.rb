require 'minitest/autorun'
require 'minitest/pride'

def freq(sample_dates, **kwargs)
  result = []
  match_date = [kwargs[:month], kwargs[:day], kwargs[:year]]
  match_date = match_date.map do |part|
    if part.nil?
      part = '*'
    else
      part = part
    end
  end.join('/')

  sample_dates.each do |date|
    !kwargs[:month].nil? ? month = date.split('/').first : month = '*'
    !kwargs[:day].nil? ? day = date.split('/')[1] : day = '*'
    !kwargs[:year].nil? ? year = date.split('/').last : year = '*'

    date = [month, day, year].join('/')

    if date == match_date
      result << date
    end
  end
  result.length
end

class DateTest < Minitest::Test
  def setup
    @dates = [
        "1/1/2019",
        "11/14/2019",
        "12/26/2019",
        "1/1/2020",
        "1/19/2020",
        "2/11/2020",
        "2/26/2020",
        "3/11/2020",
        "4/5/2020",
        "4/11/2020",
        "4/14/2020",
        "4/26/2020",
    ]
  end

  def test_it_can_return_number_of_matching_months
    assert_equal freq(@dates, month:'3'), 1
  end

  def test_it_can_return_number_of_matching_days
    assert_equal freq(@dates, day:'11'), 3
  end

  def test_it_can_return_number_of_matching_years
    assert_equal freq(@dates, year:'2019'), 3
  end

  def test_it_can_return_number_of_matching_for_many_inputs
    assert_equal freq(@dates, month: '1', year:'2020'), 2
    assert_equal freq(@dates, day: '26', year:'2020'), 2
  end
end
