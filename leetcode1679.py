# 1679. Max Number of K-Sum Pairs
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums and an integer k.
#
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
#
# Return the maximum number of operations you can perform on the array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:
#
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

from typing import List, Optional


from collections import defaultdict
class Solution(object):
    def maxOperations(self, nums, k):
        # O(n), create dict of seen values and check for existence/removal while iterating
        ans = 0
        seen = defaultdict(int)
        for b in nums:
            a = k - b # Explain: a + b = k  =>  a = k - b
            if seen[a] > 0:
                ans += 1
                seen[a] -= 1
            else:
                seen[b] += 1
        return ans


class mySolution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # O(n), create hash table with values as keys and set(index) as value
        # iterate through nums and find complement in hash table, removing index value from values

        # create dict of nums -> set(index)
        nums_idxs = {}
        for i, n in enumerate(nums):
            indexes = nums_idxs.get(n, set())
            indexes.add(i)
            nums_idxs[n] = indexes

        ops = 0
        for n in nums:
            comp = k - n
            if (comp in nums_idxs and n in nums_idxs and n == comp and len(nums_idxs[comp]) > 1) or (comp in nums_idxs and  n in nums_idxs and n != comp):
                nums_idxs[comp].pop()
                nums_idxs[n].pop()
                ops += 1

                # remove key if no indexes left in set
                if len(nums_idxs[comp]) == 0:
                    nums_idxs.pop(comp)
                if n != comp and len(nums_idxs[n]) == 0:
                    nums_idxs.pop(n)

        return ops


class testcase1:
    nums = [1, 2, 3, 4]
    k = 5
    output = 2

class testcase2:
    nums = [3, 1, 3, 4, 3]
    k = 6
    output = 1

class testcase3:
    nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
    k = 2
    output = 2

class testcase4:
    nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
    k = 3
    output = 4


# ai generated
class testcase5:
    nums = [1, 1, 1, 1, 1]
    k = 2
    output = 2 # original ai answer = 6, wrong


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.maxOperations(testcase1.nums, testcase1.k)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.maxOperations(testcase2.nums, testcase2.k)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.maxOperations(testcase3.nums, testcase3.k)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.maxOperations(testcase4.nums, testcase4.k)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")

    # test example 5
    result5 = soln.maxOperations(testcase5.nums, testcase5.k)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {testcase5.output == result5}")