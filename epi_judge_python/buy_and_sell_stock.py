from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    min_price_so_far, max_profit = float('inf'), 0.0
    # min_price_so_far = 0.0
    print(min_price_so_far)
    for price in prices:
        max_profit_so_far = price - min_price_so_far
        max_profit = max(max_profit_so_far, max_profit)
        min_price_so_far = min(price, min_price_so_far)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
