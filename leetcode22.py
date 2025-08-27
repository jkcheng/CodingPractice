# 22. Generate Parentheses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
# 1 <= n <= 8

from typing import List,Optional


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(openers, closers, s):
            # if length of s == n*2, return solution
            if len(s) == n * 2:
                ans.append(s)
                return

            # if invalid, return nothing?
            if closers > openers:
                return

            # add opener if available
            if openers < n:
                dfs(openers + 1, closers, s + '(')

            # add closers if available
            if closers < n:
                dfs(openers, closers + 1, s + ')')

        ans = []
        dfs(0, 0, '')

        return ans


class mySolution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtrack, stack:

        def backtrack(openers, closers, path):
            # add valid combination to answer
            if openers == n and closers == n:
                ans.append(path)
                return

            # recurse on adding more openers
            if openers < n:
                backtrack(openers + 1, closers, path + '(')

            # recurse on adding more closers
            if closers < n and closers < openers:
                backtrack(openers, closers + 1, path + ')')

        ans = []
        path = ''
        backtrack(0, 0, '')
        return ans


class testcase1:
    n = 3
    output = ["((()))","(()())","(())()","()(())","()()()"]

class testcase2:
    n = 1
    output = ["()"]

# ai generated
class testcase3:
    n = 2
    output = ["(())","()()"]

class testcase4:
    n = 4
    output = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.generateParenthesis(testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.generateParenthesis(testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.generateParenthesis(testcase3.n)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.generateParenthesis(testcase4.n)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")