# 714. Best Time to Buy and Sell Stock with Transaction Fee
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
#
# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
#
# Note:
#
# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.
#
#
# Example 1:
#
# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Example 2:
#
# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
#
#
# Constraints:
#
# 1 <= prices.length <= 5 * 104
# 1 <= prices[i] < 5 * 104
# 0 <= fee < 5 * 104

from typing import List, Optional

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solutions/201603/python-greedy-is-good-by-sirius930-2c5t
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n < 2:
             return 0
        ans = 0
        minimum = prices[0]
        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i] - fee - minimum
                minimum = prices[i] - fee
        return ans

class mySolution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        return


class testcase1:
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    output = 8

class testcase2:
    prices = [1, 3, 7, 5, 10, 3]
    fee = 3
    output = 6


if __name__ == '__main__':
    # create Solution instance
    soln = Solution()

    # test example 1
    result1 = soln.maxProfit(testcase1.prices, testcase1.fee)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.maxProfit(testcase2.prices, testcase2.fee)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")