# 39. Combination Sum
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
#
#
#
# Example 1:
#
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:
#
# Input: candidates = [2], target = 1
# Output: []
#
#
# Constraints:
#
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

from typing import List,Optional

# at each iteration, choose between adding candidate at current index or not including it
# decision tree looks like:
# 1. left path = all solutions with FIRST candidate[0], right_path = all solutions WITHOUT first candidate[0]
# 2. left_path = all solutions with SECOMD candidate[0], right_path = all solutions WITHOUT second candidate[0]
# 3. etc...
from typing import List, Optional


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(vals, idx, target):
            if sum(vals) == target:
                ans.append(vals)
                return

            if sum(vals) < target:
                # solutions with another copy of candidates[idx]
                c = candidates[idx]
                backtrack(vals + [c], idx, target)

                # try solutions without another copy of candidates[idx]
                for i in range(idx + 1, len(candidates)):
                    c = candidates[i]
                    backtrack(vals + [c], i, target)

        backtrack([], 0, target)
        return ans

# alternate code for similar solution
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(vals, idx, total):
            if total == target:
                ans.append(vals)
                return

            if idx >= len(candidates) or total > target:
                return

            # solutions with another copy of candidates[idx]
            c = candidates[idx]
            backtrack(vals + [c], idx, total + c)

            # try solutions without another copy of candidates[idx]
            backtrack(vals.copy(), idx + 1, total)

        backtrack([], 0, 0)
        return ans


class mySolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking: try repeatedly adding candidates up to sum
        # backtrack and try another candidate when exceeding sum

        def backtrack(i, total, combo):  # 3, 0, []
            # add combination to answer set if target found
            if total == target:
                ans.append(combo)
                return

            # backtrack
            if total > target:
                return

            # continue
            while i < len(candidates):
                # for i in range(len(candidates)):
                c = candidates[i]  # 7
                backtrack(i, total + c, combo + [c])
                i += 1

        ans = []
        # backtrack
        backtrack(0, 0, [])

        return ans


class testcase1:
    candidates = [2, 3, 6, 7]
    target = 7
    output = [[2, 2, 3], [7]]

class testcase2:
    candidates = [2, 3, 5]
    target = 8
    output = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

class testcase3:
    candidates = [2]
    target = 1
    output = []


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.combinationSum(testcase1.candidates, testcase1.target)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.combinationSum(testcase2.candidates, testcase2.target)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.combinationSum(testcase3.candidates, testcase3.target)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")