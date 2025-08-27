# 76. Minimum Window Substring
# Solved
# Hard
# Topics
# Companies
# Hint
# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character in t (including duplicates)
# is included in the window. If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
#
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
# Constraints:
#
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?

from typing import List


# O(m + n): sliding window comparing substring of s to a hashmap of character counts in t
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # create hashmap of t
        chars = {}
        for c in t:
            chars[c] = chars.get(c, 0) + 1

        # scan s
        l, r = 0, 0
        minsize = float('inf')
        found = False
        chars_have = 0
        ansr, ansl = 0, 0
        for r in range(len(s)):
            # check right character
            sc = s[r]
            if sc in chars:
                chars[sc] -= 1

            # check if char count satisfied
            if sc in chars and chars[sc] == 0:  # needs to be exact match to only count once
                chars_have += 1

            # try to shrink valid window
            while chars_have == len(chars):
                # indicate window found
                found = True

                # remove left char if possible
                if (s[l] in chars) and (chars[s[l]] + 1 <= 0):
                    chars[s[l]] += 1
                elif (s[l] in chars) and (chars[s[l]] + 1 > 0):  # if non-removable
                    break

                l += 1

            # record window
            if (chars_have == len(chars)) and (r - l + 1 < minsize):
                minsize = r - l + 1
                ansr = r
                ansl = l

        return s[ansl:ansr + 1] if found else ''

class mySolution:
    def minWindow(self, s: str, t: str) -> str:
        # create hash table for count of chars
        charcount = {}
        for c in t:
            charcount[c] = charcount.get(c,0) + 1

        # track number of total characters satisfied
        need = len(charcount)

        # sliding window parsing of s
        l, r = 0, 0
        have = 0
        ans = ''
        windowsize = len(s)+1
        while r < len(s):
            # check if char is needed
            cr = s[r]
            if cr in charcount:
                charcount[cr] -= 1
                # track number of satisfied chars
                if charcount[cr] == 0:
                    have += 1

            # try to shrink window if all chars satisfied
            while have == need: # and l < r:
                cl = s[l]
                if cl in charcount:
                    if charcount[cl] + 1 > 0:
                        # stop shrinking window
                        # ans = s[l:r+1] error?
                        break
                    else:
                        charcount[cl] += 1
                l += 1

            # check window
            if have == need and (r-l+1 < windowsize):
                windowsize = min(windowsize, r-l+1)
                ans = s[l:r+1]

            # grow window
            r += 1

        return ans


class testcase1:
    s = "ADOBECODEBANC"
    t = "ABC"

class testcase2:
    s = "a"
    t = "a"

class testcase3:
    s = "a"
    t = "aa"

class testcase4:
    s = "bbba"
    t = "ba"

class testcase5:
    s = "ab"
    t = "a"