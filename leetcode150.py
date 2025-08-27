# 150. Evaluate Reverse Polish Notation
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
# Evaluate the expression. Return an integer that represents the value of the expression.
#
# Note that:
#
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
#
#
# Example 1:
#
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
#
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:
#
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
# Constraints:
#
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        return

class mySolution:
    # push numbers to a stack
    # immediately evaluate operator on top two values on stack, then push result back to stack
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []

        for c in tokens:
            # perform operation, push result back to stack
            if c in operators:
                n2 = stack.pop()
                n1 = stack.pop()
                if c == '+':
                    stack.append(n1+n2)
                elif c == '-':
                    stack.append(n1-n2)
                elif c == '*':
                    stack.append(n1*n2)
                elif c == '/':
                    # truncate toward zero
                    # -5/2
                    stack.append(int(n1/n2))
            else:
                stack.append(int(c))

        return stack[-1]

class testcase1:
    tokens = ["2", "1", "+", "3", "*"]
    output = 9

class testcase2:
    tokens = ["4", "13", "5", "/", "+"]
    output = 6

class testcase3:
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    output = 22

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # Test with example 1
    result1 = soln.evalRPN(testcase1.tokens)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # Test with example 2
    result2 = soln.evalRPN(testcase2.tokens)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # Test with example 3
    result3 = soln.evalRPN(testcase3.tokens)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")