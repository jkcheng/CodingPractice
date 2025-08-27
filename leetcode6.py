# 6. Zigzag Conversion
# Solved
# Medium
# Topics
# Companies
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
#
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

# https://leetcode.com/problems/zigzag-conversion/solutions/2628318/python-solution-template-method-with-explanation
# https://leetcode.com/problems/zigzag-conversion/solutions/124059/thinking-process-java-python

from typing import List

class Solution(object):
    def convert(self, s, numRows):

        return

class mySolution(object):
    def convert(self, s, numRows):
        # O(n), build template indexing for which row each char should be sorted to
        # iterate through string and build final string each row at time using template

        # build template
        template = list(range(numRows)) + list(range(numRows-2,0,-1))

        # create list to hold string
        ans = ['']*len(s)
        # iterate through string and build list
        # for


        return

class testcase1:
    s = "PAYPALISHIRING"
    numRows = 3

class testcase2:
    s = "PAYPALISHIRING"
    numRows = 4