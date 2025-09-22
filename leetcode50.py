# 50. Pow(x, n)
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
#
#
# Example 1:
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
# Example 3:
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#
#
# Constraints:
#
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104

from typing import List, Optional


# O(logn): recursively multiply number with itself until n//2 reaches 1, then multiply by basex one extra time if n was odd
# e.g.: x^7 = x^3*x^3*x
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x == 0 special case
        if x == 0:
            return 0
        # n == 0 special case
        if n == 0:
            return 1

        # check if n is odd or negative
        is_odd = (n % 2 == 1)
        is_neg = (n < 0)
        n = abs(n)

        res = self.myPow(x, n // 2)
        if is_odd:
            res = res * res * x
        else:
            res = res * res

        return 1 / res if is_neg else res


class mySolution:
    def myPow(self, x: float, n: int) -> float:
        # O(logn): repeatedly multiply x by itself (squaring with each iteration)
        # e.g. x*x -> (x*x)*(x*x) -> 2 -> 4 -> 16
        # exponent doubles every loop
        # 2*2 == 4 2^2
        # 4*4 == 16 -> 2^4
        # 16*16 == 256 -> 2^8

        if n == 0:
            return 1

        ex = 1
        num = x
        while ex * 2 <= abs(n):
            num *= num
            ex *= 2

        # # TLE, iterate abs(n)-ex times, but abs(n)-ex might still be large
        # diff = abs(n)-ex
        # for _ in range(diff):
        #     num *= x
        # instead, recursively call pow
        new_n = abs(n) - ex
        if n > 0:
            num = num * self.myPow(x, new_n)
        else:
            num = (1 / num) * self.myPow(x, -new_n)

        return num


class testcase1:
    x = 2.00000
    n = 10
    output = 1024.00000

class testcase2:
    x = 2.10000
    n = 3
    output = 9.26100

class testcase3:
    x = 2.00000
    n = -2
    output = 0.25000


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.myPow(testcase1.x, testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.myPow(testcase2.x, testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.myPow(testcase3.x, testcase3.n)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

