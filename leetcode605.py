# 605. Can Place Flowers
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
#
#
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
# Constraints:
#
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

from typing import List, Optional


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        return


class mySolution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # O(n), scan array and check i, i-1, i+1 and decrement n if all three index values are 0
        # return True when n == 0 and False if n != 0 and end of array is reached

        # # append 0 to ends of flowerbed to facilitate checking
        # flowerbed = [0] + flowerbed + [0]

        # for i in range(1,len(flowerbed)-1):
        #     if not any([flowerbed[i-1],flowerbed[i],flowerbed[i+1]]):
        #         flowerbed[i] = 1
        #         n -= 1
        #     if n <= 0:
        #         return True

        # direct checking without modifying flowerbed
        for i in range(len(flowerbed)):
            before = 0 if i == 0 else flowerbed[i - 1]
            after = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
            if not any((before, flowerbed[i], after)):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True

        return False


class testcase1:
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    output = True

class testcase2:
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    output = False

class testcase3:
    flowerbed = [0, 0, 0, 0, 0, 1, 0, 0]
    n = 0
    output = True

# ai generated
class testcase4:
    flowerbed = [0, 0, 1, 0, 1]
    n = 1
    output = True

class testcase5:
    flowerbed = [0, 0, 0, 0, 1]
    n = 1
    output = True


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.canPlaceFlowers(testcase1.flowerbed, testcase1.n)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.canPlaceFlowers(testcase2.flowerbed, testcase2.n)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.canPlaceFlowers(testcase3.flowerbed, testcase3.n)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.canPlaceFlowers(testcase4.flowerbed, testcase4.n)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = soln.canPlaceFlowers(testcase5.flowerbed, testcase5.n)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")