# 322. Coin Change
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
#
# Example 1:
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Example 3:
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
# Constraints:
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

from typing import List, Optional

# 1D DP: dp array represents min number of coins to produce amount dp[i] (-1 if dp[i] is impossible to reach)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (
                    amount + 1)  # initialize dp array with amount+1, can't use more coins than amount so this is larger than the solution
        # base case
        dp[0] = 0

        # iterate up to amount and check the minimum number of coins needed to produce amount with each of the available coins
        for i in range(1, amount + 1):
            for c in coins:
                # if current_amount - c is non-negative, then we check previous dp min coins value
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        # return dp value if it is less than the initial value
        return dp[-1] if dp[-1] < amount + 1 else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1d dp: maintain dp array with dp[i] = min_coins that add up to i amount
        # concept: for each coin in coins[i], the min_coins needed to add up to i amount is min_coins(amount-coint)
        # e.g. for amount 11 and using a coin worth 5, min_coins(11) = min_coins(11-5)

        dp = [0] * (amount + 1)
        # bottom-up, build up dp array of minimum coins that add up to i amount
        for i in range(1, len(dp)):
            mincoins = float('inf')
            # loop through coins to find best final coin
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] > -1:
                    mincoins = min(mincoins, 1 + dp[i - coin])

            # set dp[i] to minimum coins found
            if mincoins < float('inf'):
                dp[i] = mincoins
            else:
                dp[i] = -1

        return dp[-1]


class testcase1:
    coins = [1, 2, 5]
    amount = 11
    output = 3

class testcase2:
    coins = [2]
    amount = 3
    output = -1

class testcase3:
    coins = [1]
    amount = 0
    output = 0

# ai generated
class testcase4:
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    amount = 202
    output = 2

class testcase5:
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    amount = 203
    output = 3 # ai gen originally -1, incorrect


if __name__ == "__main__":
    # create Solution instance
    soln = Solution()

    # test example 1
    result1 = soln.coinChange(testcase1.coins, testcase1.amount)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.coinChange(testcase2.coins, testcase2.amount)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.coinChange(testcase3.coins, testcase3.amount)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.coinChange(testcase4.coins, testcase4.amount)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = soln.coinChange(testcase5.coins, testcase5.amount)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")