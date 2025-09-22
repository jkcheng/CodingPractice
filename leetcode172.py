# 172. Factorial Trailing Zeroes
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer n, return the number of trailing zeroes in n!.
#
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:
#
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Example 3:
#
# Input: n = 0
# Output: 0
#
#
# Constraints:
#
# 0 <= n <= 104
#
#
# Follow up: Could you write a solution that works in logarithmic time complexity?

from typing import List, Optional


class Solution:
    def trailingZeroes(self, n: int) -> int:


        return


class mySolution:
    def trailingZeroes(self, n: int) -> int:
        # https://www.purplemath.com/modules/factzero.htm
        # count the number of times 5 appears as a factor in the factorial
        # implement this by integer dividing by increasing powers of 5 and adding up the results
        # alternatively, repeatedly integer dividing by 5

        # dividing by increasing powers of 5
        zeros = 0
        res = 1  # unused initial state
        power = 1
        while res > 0:
            res = n // (5 ** power)
            zeros += res
            power += 1

        return zeros


class mySolution2:
    def trailingZeroes(self, n: int) -> int:
        # https://www.purplemath.com/modules/factzero.htm
        # count the number of times 5 appears as a factor in the factorial
        # implement this by integer dividing by increasing powers of 5 and adding up the results
        # alternatively, repeatedly integer dividing by 5

        # recursively dividing by 5
        if n > 0:
            return n//5 + self.trailingZeroes(n//5)
        else:
            return 0


class testcase1:
    n = 3
    output = 0

class testcase2:
    n = 5
    output = 1

class testcase3:
    n = 0
    output = 0

# ai generated
class testcase4:
    n = 1
    output = 0

class testcase5:
    n = 2
    output = 0


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.trailingZeroes(testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.trailingZeroes(testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.trailingZeroes(testcase3.n)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.trailingZeroes(testcase4.n)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = soln.trailingZeroes(testcase5.n)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")