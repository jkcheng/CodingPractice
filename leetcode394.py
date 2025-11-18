# 394. Decode String
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#
# The test cases are generated so that the length of the output will never exceed 105.
#
#
#
# Example 1:
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#
#
# Constraints:
#
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].

from typing import List, Optional

# https://leetcode.com/problems/decode-string/solutions/586930/explained-python-solution-using-single-s-dmoj
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():     # curNum*10+int(c) is helpful in keep track of more than 1 digit number
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString


class mySolution:
    def decodeString(self, s: str) -> str:
        # O(n?), O(10*n?), stack, parse chars and nums in s and add to stack
        # pop values from stack when encountering ] and multiply popped chars by n and push back to stack
        # join stack chars together and return string at end

        stack = []
        n = 0
        for c in s:
            # add all non-ending brackets to stack
            if c != ']':
                stack.append(c)
            # pop stack values to extract substr to repeat and int
            # use '[' as delimiter between substr chars and int
            else:
                # extract substr chars
                chars = []
                while len(stack) > 0 and stack[-1] != '[':
                    chars.append(stack.pop())
                substr = ''.join(reversed(chars))
                # remove '['
                stack.pop()
                # extract int
                digits = []
                while len(stack) > 0 and stack[-1].isdigit():
                    digits.append(stack.pop())
                n = int(''.join(reversed(digits)))
                # construct repeated substr and push back to stack
                stack.append(substr * n)

        return ''.join(stack)


class testcase1:
    s = "3[a]2[bc]"
    output = "aaabcbc"

class testcase2:
    s = "3[a2[c]]"
    output = "accaccacc"

class testcase3:
    s = "2[abc]3[cd]ef"
    output = "abcabccdcdcdef"

# ai generated
class testcase4:
    s = "2[abc]3[cd]efg"
    output = "abcabccdcdcdefg"

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.decodeString(testcase1.s)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.decodeString(testcase2.s)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.decodeString(testcase3.s)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.decodeString(testcase4.s)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")