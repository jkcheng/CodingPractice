# 135. Candy
# Hard
# Topics
# Companies
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.
#
#
#
# Example 1:
#
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:
#
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
#
#
# Constraints:
#
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

# https://leetcode.com/problems/candy/solutions/1300194/python-o-n-time-solution-explained

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        return


class mySolution:
    def candy(self, ratings: List[int]) -> int:
        # O(n), two passes
        candies = [1]*len(ratings)
        for i,r in enumerate(ratings):
            if i == 0:
                left = float('inf')
            else:
                left = ratings[i-1]

            if r > left and i > 0:
                candies[i] = candies[i-1]+1
            else:
                candies[i] = 1

        for i in reversed(range(len(ratings))):
            if i == len(ratings)-1:
                right = float('inf')
            else:
                right = ratings[i+1]

            if ratings[i] > right and i < len(ratings)-1:
                if candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1]+1

        return sum(candies)


class testcase1:
    ratings = [1, 0, 2]

class testcase2:
    ratings = [1, 2, 2]

class testcase3:
    ratings = [0, 0, 0]

class testcase4:
    ratings = [1, 2, 3, 3, 3]

class testcase5:
    ratings = [5, 4, 3, 2, 1]

class testcase6:
    ratings = [1, 2, 4, 3, 2, 1, 2]

class testcase7:
    ratings = [1,3,4,5,2] # 11