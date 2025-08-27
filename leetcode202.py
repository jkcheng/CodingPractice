# 202. Happy Number
# Solved
# Easy
# Topics
# Companies
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
#
#
#
# Example 1:
#
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:
#
# Input: n = 2
# Output: false
#
#
# Constraints:
#
# 1 <= n <= 231 - 1

from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:

        return


class mySolution:
    def isHappy(self, n: int) -> bool:
        # 4, 16, 37, 58, 25+64 = 89, 72+81 = 153, 1+25+9 = 35, 15+25 = 35
        # use hash set to keep track of seen values
        # False if squared sum is in seen values, True if 1
        seen = set()
        num = n
        # can we get away with just checking previous?
        prev = n
        while num > 0:
            # square digits in number
            squaredsum = 0
            for c in str(num):
                i = int(c)
                squaredsum += i**2

            # check if result is seen or 1
            # if squaredsum in seen:
            if squaredsum == prev:
                return False
            elif squaredsum == 1:
                return True

            prev = squaredsum
            # seen.add(squaredsum)
            num = squaredsum

class testcase1:
    n = 19

class testcase2:
    n = 2

class testcase3:
    n = 9870
