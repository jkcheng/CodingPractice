# 1249. Minimum Remove to Make Valid Parentheses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '(' , ')', or lowercase English letter.

from typing import List, Optional

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        return


class mySolution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, c in enumerate(s):
            if c == ')' and len(stack) > 0 and stack[-1][0] == '(':
                stack.pop()
            elif c in ('(', ')'):
                stack.append((c, i))

        removed = [x[1] for x in stack]
        output = ['']
        for i, c in enumerate(s):
            if i not in removed:
                output.append(c)

        return ''.join(output)

class mySolution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        # O(n), stack, list
        # convert s to list, maintain stack of indexes to invalid parentheses
        # when closing encountered, pop top opening parenthesis from stack

        list_s = list(s)
        stack = []
        for i in range(len(list_s)):
            c = list_s[i]
            if c in ('(', ')'):
                # remove latest opening if closing encountered
                if c == ')' and len(stack) > 0 and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((c, i))

        # remove invalid parentheses from s
        for c, i in stack:
            list_s[i] = ''

        return ''.join(list_s)


class testcase1:
    s = "lee(t(c)o)de)"
    output = ["lee(t(c)o)de", "lee(t(co)de)" , "lee(t(c)ode)"]

class testcase2:
    s = "a)b(c)d"
    output = ["ab(c)d"]

class testcase3:
    s = "))(("
    output = [""]


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.minRemoveToMakeValid(testcase1.s)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 in testcase1.output}")

    # test example 2
    result2 = soln.minRemoveToMakeValid(testcase2.s)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 in testcase2.output}")