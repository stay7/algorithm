"""
2021-02-16
[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
121. Best Time to Buy and Sell Stock
"""

import sys
from typing import List


# 효율적으로 코딩한 것 같다 O(2n)
# 근데 느리네..?
# Runtime 1180 ms (15.29%)
# Memory 25.5 MB (7.73% )
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = [0 for i in range(len(prices))]
        maxPrice = prices[-1]

        for i in range(len(prices)):
            price = prices[len(prices)-i - 1]
            if maxPrice < price:
                maxPrice = price
            out[len(prices)-i-1] = maxPrice

        minPrice = prices[0]
        for i in range(len(prices)):
            price = prices[i]
            if minPrice > price:
                minPrice = price
            out[i] -= minPrice

        return max(out)


# 코드는 더 짧고 직관적인데 생각보다 많이 빠르지는 않네..?
# Runtime 1092 ms (30.89%)
# Memory 25.2 MB (35.68%)
class BetterSolution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price-min_price)
        return profit


if __name__ == "__main__":
    prices = [7, 6, 4, 3, 1]
    print(BetterSolution().maxProfit(prices))
