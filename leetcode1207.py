# 1207. Unique Number of Occurrences
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
#
#
#
# Example 1:
#
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:
#
# Input: arr = [1,2]
# Output: false
# Example 3:
#
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#
#
# Constraints:
#
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

from typing import List, Optional


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}

        # create a hash map
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        if len(set(dic.values())) != len(set(arr)):
            return False
        return True


class mySolution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # O(n), O(n) space, count seen values in dict, check values of dict for uniqueness
        # O(nlogn), no extra space, sort in-place and store counts in array

        # O(n), using dict
        counts = {}

        for n in arr:
            counts[n] = counts.get(n, 0) + 1

        valueset = set(counts.values())
        # check if converting counts.values() into set results in same length, meaning all values unique
        return len(valueset) == len(counts.values())

class testcase1:
    arr = [1,2,2,1,1,3]
    output = True

class testcase2:
    arr = [1,2]
    output = False

# ai generated
class testcase3:
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    output = True


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.uniqueOccurrences(testcase1.arr)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.uniqueOccurrences(testcase2.arr)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.uniqueOccurrences(testcase3.arr)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")