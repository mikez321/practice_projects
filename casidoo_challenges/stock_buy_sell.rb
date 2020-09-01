require 'minitest/autorun'
require 'minitest/pride'

# Given an array of numbers that represent stock prices (where each number is
# the price for a certain day), find 2 days when you should buy and sell your
# stock for the highest profit.
#
# Example:
#
# stockBuySell([110, 180, 260, 40, 310, 535, 695])
# “buy on day 4, sell on day 7”

def stock_buy_sell(prices)
  "buy on day #{low_day(prices)}, sell on day #{high_day(prices)}"
end

def low_day(prices)
  prices.index(prices.min) + 1
end

def high_day(prices)
  prices.index(prices.max) + 1
end

class StockBuySellTest < Minitest::Test

  def test_it_can_say_when_to_buy_and_sell
    expected = 'buy on day 4, sell on day 7'
    assert_equal expected, stock_buy_sell([110, 180, 260, 40, 310, 535, 695])
  end
end
