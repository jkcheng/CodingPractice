# 1137. N-th Tribonacci Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
#
#
#
# Example 1:
#
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:
#
# Input: n = 25
# Output: 1389537
#
#
# Constraints:
#
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

from typing import List, Optional

# https://leetcode.com/problems/n-th-tribonacci-number/solutions/1482837/python-2-solutions-dp-matrix-power-expla-d72y
class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c

        return c


class mySolution:
    def tribonacci(self, n: int) -> int:
        # O(n), 1D DP, bottom-up
        # create array of length n and update each index value T[n] = T[n-3] + T[n-2] + T[n-3]

        T = [0] * (n + 1)
        for i in range(n + 1):
            if i == 0:
                T[i] = 0
            elif i == 1 or i == 2:
                T[i] = 1
            else:
                T[i] = T[i - 1] + T[i - 2] + T[i - 3]

        return T[-1]

        # # saving space, use only constant variables
        # Tminus1 = 1
        # Tminus2 = 1
        # Tminus3 = 0

        # # special cases when n < 3
        # if n == 0:
        #     return Tminus3
        # elif n == 1 or n == 2:
        #     return Tminus1
        # else: # n >= 3, update values
        #     for i in range(3,n+1):
        #         Tnew = Tminus1 + Tminus2 + Tminus3
        #         Tminus3 = Tminus2
        #         Tminus2 = Tminus1
        #         Tminus1 = Tnew

        #     return Tnew

        # # recursive?
        # if n == 0:
        #     return 0
        # elif n == 1 or n == 2:
        #     return 1
        # else:
        #     return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)


class testcase1:
    n = 4
    output = 4

class testcase2:
    n = 25
    output = 1389537

class testcase3:
    n = 37
    output = 2082876103


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.tribonacci(testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.tribonacci(testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.tribonacci(testcase3.n)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")