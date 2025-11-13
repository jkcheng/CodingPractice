# 2390. Removing Stars From a String
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s, which contains stars *.
#
# In one operation, you can:
#
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
#
# Note:
#
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.
#
#
# Example 1:
#
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".
# Example 2:
#
# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters and stars *.
# The operation above can be performed on s.

from typing import List, Optional

class Solution:
    def removeStars(self, s: str) -> str:

        return


class mySolution:
    def removeStars(self, s: str) -> str:
        # O(n), runtime and space, stack
        # create stack of chars, remove top char from stack when * encountered

        output = []
        for c in s:
            if c == '*' and len(output) > 0:
                output.pop()
            # note: only works because of problem constraints
            # if more * than removable chars (i.e. 'a**b' then this will append '*' to output)
            # change to elif c != '*' to handle this
            else:
                output.append(c)

        return ''.join(output)


class testcase1:
    s = "leet**cod*e"
    output = "lecoe"

class testcase2:
    s = "erase*****"
    output = ""

# ai generated
class testcase3:
    s = "a**b"
    output = "b"


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.removeStars(testcase1.s)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.removeStars(testcase2.s)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.removeStars(testcase3.s)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")