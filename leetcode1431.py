# 1431. Kids With the Greatest Number of Candies
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
#
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
#
# Note that multiple kids can have the greatest number of candies.
#
#
#
# Example 1:
#
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# Example 2:
#
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [true,false,false,false,false]
# Explanation: There is only 1 extra candy.
# Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
# Example 3:
#
# Input: candies = [12,1,12], extraCandies = 10
# Output: [true,false,true]
#
#
# Constraints:
#
# n == candies.length
# 2 <= n <= 100
# 1 <= candies[i] <= 100
# 1 <= extraCandies <= 50

from typing import List, Optional

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        return


class mySolution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # O(n), two pass, get max value of candies and scan array
        # check if candies[i] + extraCandies >= max(candies)

        max_candies = max(candies)

        # classic if-else and list appending
        result = []
        for c in candies:
            # append result of logic statement to result list
            result.append(c + extraCandies >= max_candies)

        return result # [c + extraCandies >= max_candies for c in candies]


class testcase1:
    candies = [2,3,5,1,3]
    extraCandies = 3
    output = [True,True,True,False,True]

class testcase2:
    candies = [4,2,1,1,2]
    extraCandies = 1
    output = [True,False,False,False,False]

class testcase3:
    candies = [12,1,12]
    extraCandies = 10
    output = [True,False,True]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.kidsWithCandies(testcase1.candies, testcase1.extraCandies)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.kidsWithCandies(testcase2.candies, testcase2.extraCandies)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.kidsWithCandies(testcase3.candies, testcase3.extraCandies)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")