# 875. Koko Eating Bananas
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h hours.
#
#
#
# Example 1:
#
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:
#
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:
#
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#
#
# Constraints:
#
# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

from typing import List, Optional

# https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultima-sx6q
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def feasible(speed) -> bool:
            # return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower
            return sum((pile - 1) / speed + 1 for pile in piles) <= H  # faster

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left


class mySolution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # O(nlogn), binary search, search range between 1 and max(piles) to find min k

        # search range between k == 1 and max(piles)
        l, r = 1, max(piles)

        # binary search
        while l <= r:
            k = (l + r) // 2  # l + ((r-l)//2) to avoid int overflow
            # check if koko can finish
            # hours = 0
            # for p in piles:
                # remain = 1 if (p % k) > 0 else 0
                # hours += (p // k) + remain

            # alternative single line to check condition
            hours = sum(-(-pile // k) for pile in piles)

            if hours > h:
                l = k + 1
            else:
                r = k - 1

        return l


class testcase1:
    piles = [3, 6, 7, 11]
    h = 8
    output = 4

class testcase2:
    piles = [30, 11, 23, 4, 20]
    h = 5
    output = 30

class testcase3:
    piles = [30, 11, 23, 4, 20]
    h = 6
    output = 23


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.minEatingSpeed(testcase1.piles, testcase1.h)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.minEatingSpeed(testcase2.piles, testcase2.h)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.minEatingSpeed(testcase3.piles, testcase3.h)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")