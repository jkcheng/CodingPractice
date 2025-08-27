# 383. Ransom Note
# Solved
# Easy
# Topics
# Companies
# Given two strings ransomNote and magazine, return true if ransomNote
# can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
#
# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        return


# O(m+n): create hash map of char counts in magazine, then check ransomNote
class mySolution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        for c in magazine:
            chars[c] = chars.get(c,0) + 1

        for c in ransomNote:
            if c in chars:
                chars[c] -= 1
                if chars[c] < 0:
                    return False
            else:
                return False

        return True


# O(logn): sort then check if ransomnote in magazine
class mySolution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        sorted_ransom = ''.join(sorted(ransomNote))
        sorted_mag = ''.join(sorted(magazine))
        return ''.join(sorted(ransomNote)) in ''.join(sorted(magazine))

# O(n): using Counter
from collections import Counter
class mySolution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1 = Counter(ransomNote)
        d2 = Counter(magazine)
        # d1 & d2 returns the intersection of the hashmaps
        # if the intersection == d1, that means all the char counts in d2 >= char counts in d1
        return d1 & d2 == d1

class testcase1:
    ransomNote = "a"
    magazine = "b"

class testcase2:
    ransomNote = "aa"
    magazine = "ab"

class testcase3:
    ransomNote = "aa"
    magazine = "aab"