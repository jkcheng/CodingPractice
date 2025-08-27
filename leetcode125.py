# 125. Valid Palindrome
# Solved
# Easy
# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
# removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

from typing import List
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        return


class mySolution:
    def isPalindrome(self, s: str) -> bool:
        # using python internals, regex
        stripped = re.sub(r'[^a-z0-9]','',s.lower())
        ans = (stripped[::-1] == stripped)
        return ans

class mySolution2:
    def isPalindrome(self, s: str) -> bool:
        # using no internals, using pointers so no additional space O(n) time
        # custom is_alnum helper function using ordinals to determine if char is alpha numeric
        def is_alnum(c: str) -> bool:
            return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (
                        ord('0') <= ord(c) <= ord('9'))

        l = 0
        r = len(s)-1
        lowered_s = s.lower()
        while l < r:
            if is_alnum(lowered_s[l]) and is_alnum(lowered_s[r]) and lowered_s[l] == lowered_s[r]:
                l += 1
                r -= 1
            elif not is_alnum(lowered_s[l]):
                l += 1
            elif not is_alnum(lowered_s[r]):
                r -= 1
            else:
                return False

        return True


class testcase1:
    s = "A man, a plan, a canal: Panama"

class testcase2:
    s = "race a car"

class testcase3:
    s = " "