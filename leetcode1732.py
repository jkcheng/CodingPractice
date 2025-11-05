# 1732. Find the Highest Altitude
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
#
# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
#
#
#
# Example 1:
#
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
# Example 2:
#
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
#
#
# Constraints:
#
# n == gain.length
# 1 <= n <= 100
# -100 <= gain[i] <= 100

from typing import List, Optional

from itertools import accumulate
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # O(n), using python builtin accumulate()
        return max(accumulate(gain, initial=0))


class mySolution:
    def largestAltitude(self, gain: List[int]) -> int:
        # O(n), iterate through array and calculate cumulative sum, return highest partial sum seen

        alt = 0
        maxalt = 0
        for n in gain:
            alt += n
            maxalt = max(maxalt, alt)

        return maxalt



class testcase1:
    gain = [-5,1,5,0,-7]
    output = 1

class testcase2:
    gain = [-4,-3,-2,-1,4,3,2]
    output = 0

# ai generated
class testcase3:
    gain = [1,2,3,4,5]
    output = 15 # wrong answer originally: 5

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.largestAltitude(testcase1.gain)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.largestAltitude(testcase2.gain)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.largestAltitude(testcase3.gain)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")