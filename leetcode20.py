# 20. Valid Parentheses
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
#
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
#
# Output: true
#
# Example 3:
#
# Input: s = "(]"
#
# Output: false
#
# Example 4:
#
# Input: s = "([])"
#
# Output: true
#
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

from typing import List

class Solution:
    def isValid(self, s: str) -> bool:

        return

# use stack to track opening brackets and check if closing matches opening bracket
class mySolution:
    def isValid(self, s: str) -> bool:
        # use stack to track opening brackets and check if closing matches opening bracket
        openings = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []

        # iterate through chars and check if closing matches appropriate opening
        for c in s:
            if c not in openings:  # if c is a closing
                # top = stack[-1]
                if len(stack) > 0 and c == openings[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if len(stack) == 0 else False  # return true if stack is empty

# same idea, rewritten
class mySolution2:
    def isValid(self, s: str) -> bool:
        # use stack to track opening brackets and check if closing matches opening bracket
        openings = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []

        # iterate through chars and check if closing matches appropriate opening
        for c in s:
            # check if c is an opening
            if c in openings:
                stack.append(c)
            else: # c is closing, check if matches top of stack
                if len(stack) > 0 and c == openings[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False  # return true if stack is empty

class testcase1:
    s = "()"
    output = True

class testcase2:
    s = "()[]{}"
    output = True

class testcase3:
    s = "(]"
    output = False

class testcase4:
    s = "([])"
    output = True

class testcase5:
    s = "{}([{[])}"
    output = False

class testcase6:
    s = "{}([{[]}]"
    output = False

class testcase7:
    s = ")"
    output = False

# Test the solution
if __name__ == "__main__":
    # Create solution instance
    solution = mySolution()

    # Test with example 1
    result1 = solution.isValid(testcase1.s)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # Test with example 2
    result2 = solution.isValid(testcase2.s)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # Test with example 3
    result3 = solution.isValid(testcase3.s)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # Test with example 4
    result4 = solution.isValid(testcase4.s)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # Test with example 5
    result5 = solution.isValid(testcase5.s)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")

    # Test with example 6
    result6 = solution.isValid(testcase6.s)
    print(f"Example 6 - Expected: {testcase6.output}, Got: {result6}, Correct: {result6 == testcase6.output}")

    # Test with example 7
    result7 = solution.isValid(testcase7.s)
    print(f"Example 7 - Expected: {testcase7.output}, Got: {result7}, Correct: {result7 == testcase7.output}")
