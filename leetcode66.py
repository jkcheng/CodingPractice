# 66. Plus One
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.
#
#
#
# Example 1:
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:
#
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
#
#
# Constraints:
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

from typing import List, Optional


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


        return


class mySolution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1. convert array into int, add one, then convert back to int
        # 2. directly add one to last digit, carry one over and expand array if needed
        i = len(digits) - 1
        last_digit = digits[i] + 1
        while last_digit == 10:
            # set last digit to 0
            digits[i] = 0
            # decrement i and update last_digit
            i -= 1
            if i >= 0:
                last_digit = digits[i] + 1
            else:
                break

        # add 1 to beginning if indexed out of bounds
        if i < 0:
            digits = [1] + digits
        else:
            digits[i] = last_digit

        return digits

class mySolution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        # more concise direct incrementing of digits
        # iterate backwards, only continue iterating if digit is 9 else add 1 and stop
        for i in range(len(digits) - 1, -1, -1):
            # if digit at i is 9, set to 0 and continue iterating
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits

        # only reaches here if all digits were 9 so we didn't return early
        return [1] + digits



class testcase1:
    digits = [1,2,3]
    output = [1,2,4]

class testcase2:
    digits = [4,3,2,1]
    output = [4,3,2,2]

class testcase3:
    digits = [9]
    output = [1,0]

class testcase4:
    digits = [9,9,9]
    output = [1,0,0,0]

class testcase5:
    digits = [2,9,9,9]
    output = [3,0,0,0]

# ai generated
class testcase6:
    digits = [9,9,9,9]
    output = [1,0,0,0,0]

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.plusOne(testcase1.digits)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.plusOne(testcase2.digits)
    print(f"Example 2 = Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.plusOne(testcase3.digits)
    print(f"Example 3 = Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.plusOne(testcase4.digits)
    print(f"Example 4 = Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")

    # test example 5
    result5 = soln.plusOne(testcase5.digits)
    print(f"Example 5 = Expected: {testcase5.output}, Got: {result5}, Correct: {testcase5.output == result5}")

    # test example 6
    result6 = soln.plusOne(testcase6.digits)
    print(f"Example 6 = Expected: {testcase6.output}, Got: {result6}, Correct: {testcase6.output == result6}")