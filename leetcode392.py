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

class testcase1:
    s = "abc"
    t = "ahbgdc"

class testcase2:
    s = "axc"
    t = "ahbgdc"

class testcase3:
    s = "abc"
    t = "abcde"

class testcase4:
    s = "aec"
    t = "abcde"

