# 58. Length of Last Word
# Solved
# Easy
# Topics
# Companies
# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
#
#
# Example 1:
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

# https://leetcode.com/problems/length-of-last-word/solutions/847535/python-solution-without-split-explained

from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # O(n), using index pointers
        # set pointer at end and iterate backwards until non-empty char found
        end = len(s)-1
        while end >= 0 and s[end] == ' ':
            end -= 1
        # set begining pointer and scan until empty char found
        begin = end
        while begin >= 0 and s[begin] != ' ':
            begin -= 1

        return end-begin # return difference in indexes as length

        return


class mySolution:
    def lengthOfLastWord(self, s: str) -> int:
        # O(n), using python builtins
        return len(s.split()[-1])

class mySolution2:
    def lengthOfLastWord(self, s: str) -> int:
        # O(n), manually
        wordlen = 0
        wordfound = False
        for c in s[::-1]:
            if wordfound and c == ' ':
                break
            if c != " ":
                wordfound = True
                wordlen += 1

        return wordlen

class testcase1:
    s = "Hello World"

class testcase2:
    s = "   fly me   to   the moon  "

class testcase3:
    s = "luffy is still joyboy"