# 69. Sqrt(x)
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.
#
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
#
# Example 1:
#
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
#
#
# Constraints:
#
# 0 <= x <= 231 - 1

from typing import List, Optional

class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search range from [0,x] to find largest int n such that n**2 <= x
        l, r = 0, x

        root = None
        while l <= r:
            mid = l + ((r-l)//2) # avoid int overflow
            if mid*mid <= x:
                if root == None:
                    root = mid
                else:
                    root = max(root, mid)
                l = mid+1
            else:
                r = mid-1

        return root # if root != None else -1


class mySolution:
    def mySqrt(self, x: int) -> int:
        # # O(n): iterate i from 1 to x and check if i^2 <= x
        # for i in range(1,x):
        #     if i*i > x:
        #         break

        # return i-1

        # O(logn), binary search, search range [1,x] to find largest i where i*i <= x
        l, r = 1, x

        while l <= r:
            mid = l + ((r - l) // 2)  # avoid overflow
            if mid * mid > x:
                r = mid - 1
            else:  # mid * mid <= x
                l = mid + 1

        return r


class testcase1:
    x = 4
    output = 2

class testcase2:
    x = 8
    output = 2

class testcase3:
    x = 7
    output = 2

class testcase4:
    x = 16
    output = 4


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.mySqrt(testcase1.x)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.mySqrt(testcase2.x)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.mySqrt(testcase3.x)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.mySqrt(testcase4.x)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")