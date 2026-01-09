# 216. Combination Sum III
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
#
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
#
#
#
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# Example 3:
#
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
#
#
# Constraints:
#
# 2 <= k <= 9
# 1 <= n <= 60

from typing import List, Optional

# https://leetcode.com/problems/combination-sum-iii/solutions/843394/python-simple-solution-explained-video-c-auyv
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(num, stack, target):
            if len(stack) == k:
                if target == 0:
                    res.append(stack)
                return

            for x in range(num + 1, 10):
                if x <= target:
                    backtrack(x, stack + [x], target - x)
                else:
                    return

        backtrack(0, [], n)
        return res


class mySolution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # O(?), backtracking

        def backtrack(k, n, comb):
            # end condition
            if k == 0:
                if n == 0:  # successful combination
                    output.add(frozenset(comb))
                return

            # try remaining candidates
            for i in range(1, 10):
                # add candidate to combination and backtrack if candidates remain
                if i not in comb:
                    if k > 0 and i <= n:
                        # add candidate and try further
                        comb.add(i)
                        backtrack(k - 1, n - i, comb)

                        # remove candidate after trying
                        comb.remove(i)

            return

        output = set()
        backtrack(k, n, set())
        return [list(s) for s in output]


class testcase1:
    k = 3
    n = 7
    output = [[1,2,4]]

class testcase2:
    k = 3
    n = 9
    output = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

class testcase3:
    k = 4
    n = 1
    output = []


if __name__ == '__main__':
    # create Solution instances
    soln = mySolution()

    # test example 1
    result1 = soln.combinationSum3(testcase1.k, testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.combinationSum3(testcase2.k, testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.combinationSum3(testcase3.k, testcase3.n)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")