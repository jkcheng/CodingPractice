# 205. Isomorphic Strings
# Easy
# Topics
# Companies
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character
# while preserving the order of characters. No two characters may map to the same character,
# but a character may map to itself.
#
#
#
# Example 1:
#
# Input: s = "egg", t = "add"
#
# Output: true
#
# Explanation:
#
# The strings s and t can be made identical by:
#
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:
#
# Input: s = "foo", t = "bar"
#
# Output: false
#
# Explanation:
#
# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.
#
# Example 3:
#
# Input: s = "paper", t = "title"
#
# Output: true
#
#
#
# Constraints:
#
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        return


class mySolution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # check if set lengths are same
        if len(set(s)) != len(set(t)):
            return False

        # build mapping
        mapping = {}
        for i in range(len(s)):
            cs = s[i]
            ct = t[i]
            if cs not in mapping:
                mapping[cs] = ct
            else:
                if mapping[cs] != ct:
                    return False

        return True

class mySolution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # maintain two mappings s -> t, t -> s and check for consistency
        smap = {}
        tmap = {}

        for i in range(len(s)):
            sc = s[i]
            tc = t[i]

            if sc not in smap:
                smap[sc] = tc
            if tc not in tmap:
                tmap[tc] = sc
            if smap[sc] != tc or tmap[tc] != sc:
                return False

        return True

class testcase1:
    s = "egg"
    t = "add"

class testcase2:
    s = "foo"
    t = "bar"

class testcase3:
    s = "paper"
    t = "title"

class testcase4:
    s = "bbbaaaba"
    t = "aaabbbba"

class testcase5:
    s = "bbbaaaac"
    t = "aaabbbba"