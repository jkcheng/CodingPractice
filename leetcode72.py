# 72. Edit Distance
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
#
#
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
# Constraints:
#
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.

from typing import List, Optional


# this problem is similar to minimum path problem between word1 -> word2
# dp array is m x n array where m = len(word2)+1, n = len(word1)+1
# dp[i][j] represents min edits to convert word2[i] (1-indexed) to word1[j] (1-indexed)
# dp[i][j] can be calculated as min(dp[i-1][j-1],dp[i-1][j],dp[i]p[j-1]) if word2[i]==word1[j] (add one if letters do not match)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word2) + 1
        n = len(word1) + 1
        dp = [[0] * n for _ in range(m)]

        dp[0] = [i for i in range(n)]
        for j in range(m):
            dp[j][0] = j

        for i in range(1, m):
            for j in range(1, n):
                if word2[i - 1] != word1[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]


class mySolution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 2d dp, create array with word1 on one axis and word2 on second
        # to make implementation easier, use 1-indexing on word1 and word2
        # or imagine word1 and word2 as having an empty char at the beginning (word1[0] == '')
        # dp[i][j] represents number of operations to change word1[j] to word2[i]
        # dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + (1 if word1[j] != word2[i] else 0)

        #    '',h,o,r,s,e
        # ''[[0,1,2,3,4,5]
        # r  [1,1,2,3,4,5]
        # o  [2,2,1,2,3,4]
        # s  [3,3,2,2,3,4]]

        m = len(word2) + 1
        n = len(word1) + 1
        dp = [[0] * n for _ in range(m)]

        # base cases
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j

        for i in range(1, m):
            for j in range(1, n):
                # add 1 if current letter not the same
                # word1 and word2 are treated as 1-indexed
                if word2[i - 1] != word1[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                else: # letters are the same, min operations is the same as minDistance(word1[j-2],word2[i-2])
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]


class testcase1:
    word1 = "horse"
    word2 = "ros"
    output = 3

class testcase2:
    word1 = "intention"
    word2 = "execution"
    output = 5

class testcase3:
    word1 = "a"
    word2 = "aa"
    output = 1

class testcase4:
    word1 = ""
    word2 = "a"
    output = 1


if __name__ == "__main__":
    # create Solution instance
    soln = Solution()

    # test example 1
    result1 = soln.minDistance(testcase1.word1, testcase1.word2)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.minDistance(testcase2.word1, testcase2.word2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.minDistance(testcase3.word1, testcase3.word2)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.minDistance(testcase4.word1, testcase4.word2)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")