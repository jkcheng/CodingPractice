# 14. Longest Common Prefix
# Easy
# Topics
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # O(nm), scan every string and append to prefix if char present in all strings
        # iterate through chars in shortest word and compare to same index of other words
        shortest = min(strs, key=len)
        for i,c in enumerate(shortest):
            for others in strs:
                # if char does not match c from shortest, return slice of shortest
                if others[i] != c:
                    return shortest[:i]

        return shortest

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # O(m+nlogn), sort strings, then compare first and last strings
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i,c in enumerate(first):
            if i < len(last) and last[i] != c:
                return first[:i]

        return first


class mySolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # O(nm), scan every string and append to prefix if char present in all strings
        prefix = ''
        # iterate through chars in shortest word and compare to same index of other words
        shortest = min(strs, key=len)
        for i,c in enumerate(shortest):
            for others in strs:
                # if char does not match c from shortest, return slice of shortest
                if others[i] != c:
                    return shortest[:i]

        return shortest

class testcase1:
    strs = ["flower", "flow", "flight"]

class testcase2:
    strs = ["dog", "racecar", "car"]

class testcase3:
    strs = ["flower", "flow", "reflow"]

class testcase4:
    strs = ["flowa", "flowz", "flows"]