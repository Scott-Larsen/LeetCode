# Say you have an array for which the ith element is the price of a given stock
# on day i.

# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = -1
        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1] and buy >= 0:
                profit += prices[i] - buy
                buy = -1
            elif prices[i] < prices[i + 1] and buy < 0:
                buy = prices[i]
        if buy >= 0:
            profit += prices[-1] - buy
        return profit