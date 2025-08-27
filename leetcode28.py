# 28. Find the Index of the First Occurrence in a String
# Easy
# Topics
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
#
#
#
# Example 1:
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#
# Constraints:
#
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/3456653/beats-97-46-7-145-top-interview-question

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        return


class mySolution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        # check each substring of len(needle) within haystack
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i

        return -1

class testcase1:
    haystack = "sadbutsad"
    needle = "sad"

class testcase2:
    haystack = "leetcode"
    needle = "leeto"

class testcase3:
    haystack = "abc"
    needle = "c"

class testcase4:
    haystack = "mississippi"
    needle = "issip"