# 139. Word Break
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#
#
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

from typing import List, Optional

# dfs using str.startswith, expandable to wordbreak ii
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(s, wordDict, memo):
            if s in memo:
                return memo[s]
            if not s:
                return False

            ans = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):
                    ans.append(True)
                else:
                    ans.append(dfs(s[len(word):], wordDict, memo))

            memo[s] = any(ans)
            return any(ans)

        return dfs(s, wordDict, {})

# 1D DP solution, O(n*m) run time: maintain dp array of len(s) with dp[i] == True if dp[0:i+1] can form valid word break
# for each word in wordDict, check either s[0:i] in wordDict or dp[i-len(word)] == True AND s[i-len(word}:i+1] in wordDict
# for every i, check that the slice of s[i-len(word):i+1] is an actual word and use dp array to check if previous section of s
class mySolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            end = i+1
            for w in wordDict:
                if (     (end-len(w) >= 0 and s[end-len(w):end] == w) # current slice == word in dict
                     and (dp[i-len(w)] == True or i-len(w) < 0) # previous slice of s is valid word break OR is out of bounds
                   ):
                    dp[i] = True # mark current position i as valid word break
        return dp[-1]

class mySolution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # recursive with memoization, expandable to word break II where we return every valid combination possible
        # check whether the beginning of s contains a word from the list
        # if s starts with a word, recursively check the rest of s
        # if the end of s is reached in recursive call stack, return True
        # (end of s was reached by constructing a series of words from list)
        # memoization: use hash map to store whether end of s reachable from here

        def dfs(s, wordDict, memo):
            # if current s in memo, return prev discovered result
            if s in memo:
                return memo[s]

            # if s is empty, then return true because we reached end of original s
            if len(s) == 0:
                return True

            # recurse when a word is a prefix of s
            for word in wordDict:
                if s[0:len(word)] == word:  # can also use s.startswith(word)
                    # if recursive search returns true, we can reach end of s using current word
                    # store result as true for current s
                    if dfs(s[len(word):], wordDict, memo):
                        memo[s] = True
                        return True  # return true, no need to consider other options here
            # loop did not return early, end of s not reachable from here
            memo[s] = False
            return False

        return dfs(s, wordDict, {})

class testcase1:
    s = "leetcode"
    wordDict = ["leet","code"]
    output = True

class testcase2:
    s = "applepenapple"
    wordDict = ["apple","pen"]
    output = True

class testcase3:
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    output = False

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.wordBreak(testcase1.s, testcase1.wordDict)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.wordBreak(testcase2.s, testcase2.wordDict)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.wordBreak(testcase3.s, testcase3.wordDict)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")