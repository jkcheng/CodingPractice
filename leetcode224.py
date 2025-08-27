# 224. Basic Calculator
# Hard
# Topics
# premium lock icon
# Companies
# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
#
#
# Example 1:
#
# Input: s = "1 + 1"
# Output: 2
# Example 2:
#
# Input: s = " 2-1 + 2 "
# Output: 3
# Example 3:
#
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
#
#
# Constraints:
#
# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.

from typing import List


class Solution:
    def calculate(self, s):
        def calc(it):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))

            num, stack, sign = 0, [], "+"

            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, j = calc(it + 1)
                    it = j - 1
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack), it + 1
                it += 1
            update(sign, num)
            return sum(stack)

        return calc(0)


class mySolution:
    def calculate(self, s: str) -> int:
        # maintain a stack of elements that can be summed to obtain the solution
        # push positive numbers to stack, push subtracted numbers to stack as negative
        # recursively call calculate when encountering ()

        # recursive inner function to evaluate s from index i
        def evaluate(s, i):
            stack = []
            op = '+' # default operation to addition
            num = 0
            # use pointer to index into s, allow for skipping indexes
            while i < len(s):
                c = s[i]
                if c.isdigit(): # build number if c is digit
                    num = 10*num + int(c)
                elif c in ('-','+'): # process num based on prev op and update op
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    # reset/update values
                    num = 0
                    op = c
                elif c == '(': # recursive call for parenthesis
                    num, j = evaluate(s, i+1)
                    i = j # move pointer ahead past the evaluated inner parenthesis
                elif c == ')':
                    # update stack with final num
                    if op == '+':
                        stack.append(num)
                    elif op == '-':
                        stack.append(-num)
                    return sum(stack), i
                i += 1

            # update stack with final num
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            return sum(stack), i

        # process s and evaluate it from beginning
        s = s.replace(' ','')
        ans, idx = evaluate(s, 0)
        return ans

class testcase1:
    s = "1 + 1"
    output = 2

class testcase2:
    s = " 2-1 + 2 "
    output = 3

class testcase3:
    s = "(1+(4+5+2)-3)+(6+8)"
    output = 23

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # Test example 1
    result1 = soln.calculate(testcase1.s)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # Test example 2
    result2 = soln.calculate(testcase2.s)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # Test example 3
    result3 = soln.calculate(testcase3.s)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")
