# 1456. Maximum Number of Vowels in a Substring of Given Length
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
#
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
#
#
#
# Example 1:
#
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:
#
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:
#
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

from typing import List, Optional


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Maximum vowels i.e. ans
        ans: int = 0

        # Vowels in current window
        currCount: int = 0

        # String of vowels
        vowels: str = "aeiou"

        # Using sliding window technique to
        # calculate number of vowels in each window and
        # update the count
        for i, v in enumerate(s):
            if i >= k:
                if s[i - k] in vowels:
                    currCount -= 1
            if s[i] in vowels:
                currCount += 1
            ans = max(currCount, ans)
        return ans

class mySolution:
    def maxVowels(self, s: str, k: int) -> int:
        # O(n), sliding window, count vowels in window of size k
        # slide window to end of s and return max vowels seen

        # count vowels in initial window
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for c in s[0:k]:
            if c in vowels:
                count += 1

        # slide window to end of s
        maxcount = count
        for i in range(k, len(s)):
            # add vowel to window
            if s[i] in vowels:
                count += 1

            # remove vowel from window
            if s[i - k] in vowels:
                count -= 1

            maxcount = max(maxcount, count)

        return maxcount


class testcase1:
    s = "abciiidef"
    k = 3
    output = 3

class testcase2:
    s = "aeiou"
    k = 2
    output = 2

class testcase3:
    s = "leetcode"
    k = 3
    output = 2

# ai generated
class testcase4:
    s = "rhythms"
    k = 4
    output = 0

class testcase5:
    s = "tryhard"
    k = 4
    output = 1


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.maxVowels(testcase1.s, testcase1.k)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.maxVowels(testcase2.s, testcase2.k)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.maxVowels(testcase3.s, testcase3.k)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.maxVowels(testcase4.s, testcase4.k)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = soln.maxVowels(testcase5.s, testcase5.k)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")