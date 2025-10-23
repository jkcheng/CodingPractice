# 443. String Compression
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.
#
# Note: The characters in the array beyond the returned length do not matter and should be ignored.
#
#
#
# Example 1:
#
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:
#
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:
#
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
#
#
# Constraints:
#
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

from typing import List, Optional


class Solution:
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        while fast < len(chars):
            chars[slow] = chars[fast]
            count = 1

            # check next char
            while fast + 1 < len(chars) and chars[fast] == chars[fast + 1]:
                fast += 1
                count += 1

            # add counts to chars
            if count > 1:
                for c in str(count):
                    slow += 1
                    chars[slow] = c

            # increment pointers
            slow += 1
            fast += 1

        return slow


class mySolution:
    def compress(self, chars: List[str]) -> int:
        # O(n), use slow and fast pointers to read array and write output to array
        # count repeated characters and write count to array

        slow, fast = 0, 0
        c = chars[fast]
        count = 0
        while fast < len(chars):
            # increment count if duplicate charater
            if c == chars[fast]:
                count += 1
            elif count == 1:
                chars[slow] = c
                c = chars[fast]
                slow += 1
            else:  # write current char and count to slow pointer position
                for countc in c + str(count):
                    chars[slow] = countc
                    slow += 1
                # reset count
                count = 1
                c = chars[fast]

            fast += 1

        # write last char
        if count == 1:
            chars[slow] = c
            slow += 1
        else:
            for countc in c + str(count):
                chars[slow] = countc
                slow += 1

        return slow


class testcase1:
    chars = ["a","a","b","b","c","c","c"]
    output = 6

class testcase2:
    chars = ["a"]
    output = 1

class testcase3:
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    output = 4


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.compress(testcase1.chars)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.compress(testcase2.chars)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.compress(testcase3.chars)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")