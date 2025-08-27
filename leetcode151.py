# 151. Reverse Words in a String
# Solved
# Medium
# Topics
# Companies
# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words. Do not include any extra spaces.
#
#
#
# Example 1:
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
#
#
# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

# https://leetcode.com/problems/reverse-words-in-a-string/solutions/737124/python-2-solutions-oneliner-inplace-for-list-of-chars-explained

from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        chars = [t for t in s]
        slow, n = 0, len(s)
        for fast in range(n):
            if chars[fast] != " " or (fast > 0 and chars[fast] == " " and chars[fast - 1] != " "):
                chars[slow] = chars[fast]
                slow += 1

        # if slow == 0: return "" # not necessary due to input constraints (no empty strings)
        chars = chars[:slow - 1] if chars[-1] == " " else chars[:slow]
        chars.reverse()

        slow, m = 0, len(chars)
        for fast in range(m + 1):
            if fast == m or chars[fast] == " ":
                chars[slow:fast] = chars[slow:fast][::-1]
                slow = fast + 1

        return "".join(chars)


class mySolution:
    def reverseWords(self, s: str) -> str:
        # O(n) time, space, convert to list and reverse list
        slist = s.split()
        return ' '.join(reversed(slist))

class mySolution2:
    # O(n) time, O(1) space, reverse entire string, then reverse individual words in-place while removing extra spaces
    def reverseWords(self, s: str) -> str:
        # setup for "mutable" string
        slist = list(s)
        # trim extra spaces from string
        slist = self.trim_reverse(slist)
        slist = self.reverse_chars(slist)
        return ''.join(slist)

    # def trim_spaces(self, slist: list) -> list:
    #     # use slow & fast pointers to copy only chars and single spaces to slow pointer and skip multiple spaces
    #     slow, fast = 0, 0
    #     # skip beginning spaces
    #     while slist[fast] == ' ':
    #         fast += 1
    #
    #     while fast < len(slist):
    #         # skip consecutive spaces
    #         if fast > 0 and slist[fast] == ' ' and slist[fast-1] == ' ':
    #             fast += 1
    #             continue
    #
    #         # copy chars to beginning of list
    #         slist[slow] = slist[fast]
    #         fast += 1
    #         slow += 1
    #
    #     # handle edge case of trailing single blank space
    #     if slist[slow-1] == ' ':
    #         slist = slist[:slow-1]
    #     else:
    #         slist = slist[:slow]
    #     return slist

    def trim_reverse(self, chars: list) -> list:
        # chars = [t for t in s]
        # chars = slist
        # use slow & fast pointers to copy only chars and single spaces to slow pointer and skip multiple spaces
        slow, n = 0, len(chars)
        for fast in range(n):
            # copy char to slow ptr if letter or not consecutive blank
            if chars[fast] != ' ' or (fast > 0 and chars[fast] == ' ' and chars[fast - 1] != ' '):
                chars[slow] = chars[fast]
                slow += 1

        # if slow == 0: return "" # not necessary due the input constraints (no empty strings)
        # remove trailing single space
        if chars[-1] == ' ':
            chars = chars[:slow-1]
        else:
            chars = chars[:slow]

        # reverse in-place
        chars.reverse()
        return chars

    def reverse_chars(self, chars: list) -> list:
        # not true O(1) space, using slices to copy and reverse words
        # use slow and fast pointers to revers slices of chars
        slow, n = 0, len(chars)
        for fast in range(n+1): # range(n+1) so slicing is consistent for end of string
            # reverse previous word when space encountered or fast reaches end of string
            if fast == n or chars[fast] == ' ': # check fast == n first to avoid indexing error
                chars[slow:fast] = chars[slow:fast][::-1]
                # increment slow to next index after space
                slow = fast+1

        return chars


class testcase1:
    s = "the sky is blue"

class testcase2:
    s = "  hello world    "

class testcase3:
    s = "a good   example"

class testcase4:
    s = " 3l33tc0d3   ha  "

class testcase5:
    s = '    s  '