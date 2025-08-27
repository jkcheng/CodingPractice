# 290. Word Pattern
# Easy
# Topics
# Companies
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
#
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
#
#
# Example 1:
#
# Input: pattern = "abba", s = "dog cat cat dog"
#
# Output: true
#
# Explanation:
#
# The bijection can be established as:
#
# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:
#
# Input: pattern = "abba", s = "dog cat cat fish"
#
# Output: false
#
# Example 3:
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
#
# Output: false
#
#
#
# Constraints:
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

from typing import List


class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        words, w_to_p = s.split(' '), dict()

        if len(p) != len(words): return False
        if len(set(p)) != len(set(words)): return False  # for the case w = ['dog', 'cat'] and p = 'aa'

        for i in range(len(words)):
            if words[i] not in w_to_p:
                w_to_p[words[i]] = p[i]
            elif w_to_p[words[i]] != p[i]:
                return False

        return True


class mySolution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split s into list of words, build mapping of pattern character -> words
        # return false if pattern is violated
        words = s.split(' ')

        # return false if lengths don't match
        if len(pattern) != len(words):
            return False

        # build mapping and check consistency
        mapping = {}
        reversemap = {}
        for i,c in enumerate(pattern):
            # return false if mapping doesn't match what we've seen before
            word = words[i]
            if c not in mapping:
                mapping[c] = word
            if word not in reversemap:
                reversemap[word] = c
            if (c in mapping and mapping[c] != words[i]) or (word in reversemap and reversemap[word] != c):
                return False

        return True

class testcase1:
    pattern = "abba"
    s = "dog cat cat dog"

class testcase2:
    pattern = "abba"
    s = "dog cat cat fish"

class testcase3:
    pattern = "aaaa"
    s = "dog cat cat dog"

class testcase4:
    pattern = "abba"
    s = "dog dog dog dog"