# 374. Guess Number Higher or Lower
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
#
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns three possible results:
#
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.
#
#
#
# Example 1:
#
# Input: n = 10, pick = 6
# Output: 6
# Example 2:
#
# Input: n = 1, pick = 1
# Output: 1
# Example 3:
#
# Input: n = 2, pick = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= n <= 231 - 1
# 1 <= pick <= n

from typing import List, Optional

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:



class Solution:
    def guessNumber(self, n: int) -> int:

        return None


class mySolution:
    def guessNumber(self, n: int) -> int:
        # return num such that guess(num) == 0, where num in [1,n]
        # use binary search
        l, r = 1, n

        while l <= r:
            mid = l+(r-l)//2 # actual risk of overflow
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1: # mid > pick
                r = mid-1
            else: # mid < pick
                l = mid+1

        return None


class testcase1:
    n = 10
    pick = 6
    output = 6

class testcase2:
    n = 1
    pick = 1
    output = 1

class testcase3:
    n = 2
    pick = 1
    output = 1


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.guessNumber(testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.guessNumber(testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")