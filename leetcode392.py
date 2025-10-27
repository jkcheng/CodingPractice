# 392. Is Subsequence
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
#
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

from typing import List

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp, tp = 0, 0
        while (tp < len(t)) and (sp < len(s)):
            if t[tp] == s[sp]:
                sp += 1
            tp += 1

        # if sp == len(s):
        #     return True
        # else:
        #     return False
        return True if sp == len(s) else False


class mySolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(t) and j < len(s):
            ct = t[i]
            cs = s[j]
            if ct == cs:
                j += 1
            i += 1

        if j >= len(s):
            return True
        else:
            return False

class mySolution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        # O(n), two pointer, iterate through t and advance pointer in s if char in t matches s
        # return True if s-pointer reaches end of s, False if not

        points = 0
        for i, c in enumerate(t):
            # check if end of s reached
            if points >= len(s):
                break

            cs = s[points]
            if c == cs:
                points += 1

        return points == len(s)

import bisect
from collections import defaultdict
class mysolution3:
    def isSubsequence(self, s: str, t: str) -> bool:
        # followup:  Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
        # and you want to check one by one to see if t has its subsequence.
        # In this scenario, how would you change your code?
        # Use binary search
        places = {}
        for i, symbol in enumerate(t):
            symbol_idxes = places.get(symbol, [])
            symbol_idxes.append(i)
            places[symbol] = symbol_idxes

        current_place = 0
        for symbol in s:
            current_ind = bisect.bisect_left(places.get(symbol, []), current_place)
            if current_ind >= len(places.get(symbol, [])):
                return False
            current_place = places[symbol][current_ind] + 1

        return True

class testcase1:
    s = "abc"
    t = "ahbgdc"
    output = True

class testcase2:
    s = "axc"
    t = "ahbgdc"
    output = False

class testcase3:
    s = "abc"
    t = "abcde"
    output = True

class testcase4:
    s = "aec"
    t = "abcde"
    output = False

class testcase5:
    s = ""
    t = "ahbgdc"
    output = True

class testcase6:
    s = "b"
    t = "ahbgdc"
    output = True


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.isSubsequence(testcase1.s, testcase1.t)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.isSubsequence(testcase2.s, testcase2.t)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.isSubsequence(testcase3.s, testcase3.t)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.isSubsequence(testcase4.s, testcase4.t)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")

    # test example 5
    result5 = soln.isSubsequence(testcase5.s, testcase5.t)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {testcase5.output == result5}")

    # test example 6
    result6 = soln.isSubsequence(testcase6.s, testcase6.t)
    print(f"Example 6 - Expected: {testcase6.output}, Got: {result6}, Correct: {testcase6.output == result6}")

