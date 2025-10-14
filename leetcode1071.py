# 1071. Greatest Common Divisor of Strings
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
#
#
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
#
# Constraints:
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

from typing import List, Optional


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        return str1[:gcd(len(str1), len(str2))]


class mySolution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # first check that str1+str2 == str2+str1
        # If they both have a gcd then concat in different order should result in same str
        # greatest common string divisor will evenly divide both str1 and str2
        # find largest common denominator of len(str1), len(str2)
        # return first x characters of str1 and str2 match

        if str1 + str2 != str2 + str1:
            return ''

        # make str1 longer of two
        if len(str2) > len(str1):
            str1, str2 = str2, str1

        ls1 = len(str1)
        ls2 = len(str2)

        # find greatest common divisor by finding the remainder of dividing ls1/ls2
        # repeatedly perform larger % smaller and replace larger with result of calc
        # gcd will be larger number after larger % smaller evaluation reaches 0
        gcd = 1
        while gcd > 0:
            gcd = ls1 % ls2
            ls1 = ls2
            ls2 = gcd

        # ls1 is now length of gcd
        return str1[:ls1]

class testcase1:
    str1 = "ABCABC"
    str2 = "ABC"
    output = "ABC"

class testcase2:
    str1 = "ABABAB"
    str2 = "ABAB"
    output = "AB"

class testcase3:
    str1 = "LEET"
    str2 = "CODE"
    output = ""

class testcase4:
    str1 = "ABCDEF"
    str2 = "ABC"
    output = ""


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.gcdOfStrings(testcase1.str1, testcase1.str2)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.gcdOfStrings(testcase2.str1, testcase2.str2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.gcdOfStrings(testcase3.str1, testcase3.str2)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.gcdOfStrings(testcase4.str1, testcase4.str2)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")