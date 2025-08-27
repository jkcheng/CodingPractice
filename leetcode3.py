# 3. Longest Substring Without Repeating Characters
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        return

class mySolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, r = 0, 0
        maxsize = 0
        while r < len(s):
            rc = s[r]
            # check for new char existence
            if rc not in chars:
                chars.add(rc)
                r += 1
            else:  # try to shrink window until rc removed from set
                lc = s[l]
                chars.remove(lc)
                l += 1

            maxsize = max(maxsize, r - l)
        return maxsize

class testcase1:
    s = "abcabcbb"

class testcase2:
    s = "bbbbb"

class testcase3:
    s = "pwwkew"
