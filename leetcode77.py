# 77. Combinations
# Medium
# Topics
# premium lock icon
# Companies
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:
#
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
#
#
# Constraints:
#
# 1 <= n <= 20
# 1 <= k <= n

from typing import List,Optional


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        return


class mySolution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # backtracking: iterate from 1 to n, append next number after initial number k times, up to n
        # recurse on next number up to k times
        def backtrack(i, combo):  # i == 3, comob == (1,2)
            # check if we completed a combination with i
            combo += tuple([i])
            if len(combo) == k:
                ans.add(combo)
                return

            # try to add more items to combination
            if len(combo) <= k and i + 1 <= n:
                for j in range(i + 1, n + 1):
                    backtrack(j, combo)

        ans = set()
        for i in range(1, n + 1):
            combo = tuple()
            backtrack(i, combo)

        return sorted([list(item) for item in ans])


class testcase1:
    n = 4
    k = 2
    output = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

class testcase2:
    n = 1
    k = 1
    output = [[1]]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.combine(testcase1.n, testcase1.k)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.combine(testcase2.n, testcase2.k)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")