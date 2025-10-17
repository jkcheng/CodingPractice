# 345. Reverse Vowels of a String
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#
#
# Example 1:
#
# Input: s = "IceCreAm"
#
# Output: "AceCreIm"
#
# Explanation:
#
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#
# Example 2:
#
# Input: s = "leetcode"
#
# Output: "leotcede"
#
#
#
# Constraints:
#
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

from typing import List, Optional


class Solution:
    def reverseVowels(self, s):
        s = list(s)
        vows = set('aeiouAEIOU')
        l, r = 0, len(s) - 1
        while l <= r:
            while l <= r and s[l] not in vows: l += 1
            while l <= r and s[r] not in vows: r -= 1
            if l > r: break
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        return ''.join(s)


class mySolution:
    def reverseVowels(self, s: str) -> str:
        # O(n), O(n) space, scan string and store vowels, indices in separate list
        # replace vowles at indices with reversed vowels

        vowels = []
        indices = []
        vowel_list = {'a', 'e', 'i', 'o', 'u'}
        for i, c in enumerate(s):
            if c.lower() in vowel_list:
                vowels.append(c)
                indices.append(i)

        # replace vowels with reversed vowels
        list_s = list(s)
        for i, c in zip(indices, reversed(vowels)):
            list_s[i] = c

        return ''.join(list_s)

class mySolution2:
    def reverseVowels(self, s: str) -> str:
        # O(n), O(1) space, two-pointers
        # one pointer iterates forward, one iterates reverse
        # stop pointers at vowels and reverse positions before continuing
        # return s when pointers meet

        forward, reverse = 0, len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        list_s = list(s)
        while forward < reverse:
            if s[forward].lower() not in vowels:
                forward += 1
            if s[reverse].lower() not in vowels:
                reverse -= 1

            # swap positions and move pointers if both are at vowels
            if s[forward].lower() in vowels and s[reverse].lower() in vowels:
                list_s[forward], list_s[reverse] = list_s[reverse], list_s[forward]
                forward += 1
                reverse -= 1

        return ''.join(list_s)


class testcase1:
    s = "IceCreAm"
    output = "AceCreIm"

class testcase2:
    s = "leetcode"
    output = "leotcede"


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.reverseVowels(testcase1.s)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.reverseVowels(testcase2.s)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")