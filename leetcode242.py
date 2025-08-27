# 242. Valid Anagram
# Solved
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
#
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
#
# Output: false
#
#
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

from typing import List
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)

# manually create dict counts of characters
class mySolution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s, counts_t = {}, {}
        for c in s:
            counts_s[c] = counts_s.get(c,0) + 1

        for c in t:
            counts_t[c] = counts_t.get(c,0) + 1

        return counts_s == counts_t

class testcase1:
    s = "anagram"
    t = "nagaram"

class testcase2:
    s = "rat"
    t = "car"
