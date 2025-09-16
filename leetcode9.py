# 9. Palindrome Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
#
#
# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Constraints:
#
# -231 <= x <= 231 - 1
#
#
# Follow up: Could you solve it without converting the integer to a string?

from typing import List, Optional


class Solution:
    def isPalindrome(self, x: int) -> bool:

        return


class mySolution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        return sx == ''.join(reversed(sx))


class mySolution2:
    def isPalindrome(self, x: int) -> bool:
        # without converting to string
        reversed_x = 0
        old_x = x
        while x > 0:
            # get last digit in number and add to new number
            digit = x % 10
            reversed_x = reversed_x * 10 + digit

            # remove last digit
            x //= 10

        return reversed_x == old_x


class testcase1:
    x = 121
    output = True

class testcase2:
    x = -121
    output = False

class testcase3:
    x = 10
    output = False

# ai generated
class testcase4:
    x = 12321
    output = True

class testcase5:
    x = 123456789
    output = False


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.isPalindrome(testcase1.x)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.isPalindrome(testcase2.x)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.isPalindrome(testcase3.x)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.isPalindrome(testcase4.x)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")

    # test example 5
    result5 = soln.isPalindrome(testcase5.x)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {testcase5.output == result5}")