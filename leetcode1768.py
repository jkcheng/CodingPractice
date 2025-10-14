# 1768. Merge Strings Alternately
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.
#
#
#
# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d
#
#
# Constraints:
#
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

from typing import List, Optional


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        # index through shorter word
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])

        return ''.join(res) + word1[i + 1:] + word2[i + 1:]


class mySolution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # manual iteration: iterate through strings, append to list, convert list to string
        ans = []

        for i in range(len(word1)):
            # i in range of index for both words
            if i < len(word2):
                ans.append(word1[i])
                ans.append(word2[i])
            else: # word1 is longer
                ans.append(word1[i])

        # word2 is longer, append rest of word2
        if i+1 < len(word2):
            ans.append(word2[i+1:])

from itertools import zip_longest
class mySolution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # using zip_longest() in one line with iterator
        return ''.join(c1+c2 for c1,c2 in zip_longest(word1, word2, fillvalue=''))


class testcase1:
    word1 = "abc"
    word2 = "pqr"
    output = "apbqcr"

class testcase2:
    word1 = "ab"
    word2 = "pqrs"
    output = "apbqrs"

class testcase3:
    word1 = "abcd"
    word2 = "pq"
    output = "apbqcd"


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.mergeAlternately(testcase1.word1, testcase1.word2)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.mergeAlternately(testcase2.word1, testcase2.word2)
    print(f"Example 2 - Expected: {testcase1.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.mergeAlternately(testcase3.word1, testcase3.word2)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")