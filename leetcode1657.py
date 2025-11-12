# 1657. Determine if Two Strings Are Close
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Two strings are considered close if you can attain one from the other using the following operations:
#
# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.
#
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
#
#
#
# Example 1:
#
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# Example 2:
#
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
# Example 3:
#
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
#
#
# Constraints:
#
# 1 <= word1.length, word2.length <= 105
# word1 and word2 contain only lowercase English letters.

from typing import List, Optional


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        return


class mySolution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # O(n), check if characters of string are the same, then check if character counts are same
        # operations can be alternatively interpreted as:
        # operation 1, swap order of characters (words have the same characters)
        # operation 2, chracter frequencies can be swapped (check if frequencies are the same)

        # optimization: check for set before counting characters
        if set(word1) != set(word2):
            return False

        counts1 = {}
        counts2 = {}

        # can also use Counter() for optimized run time
        for c in word1:
            counts1[c] = counts1.get(c, 0) + 1

        for c in word2:
            counts2[c] = counts2.get(c, 0) + 1

        # return (counts1.keys() == counts2.keys()) and (sorted(counts1.values()) == sorted(counts2.values()))
        return (sorted(counts1.values()) == sorted(counts2.values()))


class testcase1:
    word1 = "abc"
    word2 = "bca"
    output = True

class testcase2:
    word1 = "a"
    word2 = "aa"
    output = False

class testcase3:
    word1 = "cabbba"
    word2 = "abbccc"
    output = True

class testcase4:
    word1 = "cabbbb"
    word2 = "abbccc"
    output = False

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.closeStrings(testcase1.word1, testcase1.word2)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.closeStrings(testcase2.word1, testcase2.word2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.closeStrings(testcase3.word1, testcase3.word2)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.closeStrings(testcase4.word1, testcase4.word2)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")