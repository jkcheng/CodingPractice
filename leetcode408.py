# Premium question, text taken from leetcode.ca
# 408 - Valid Word Abbreviation
# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.
#
# For example, a string such as "substitution" could be abbreviated as (but not limited to):
#
# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:
#
# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
#
# A substring is a contiguous non-empty sequence of characters within a string.

# Constraints:
#
# 1 <= word.length <= 20
# word consists of only lowercase English letters.
# 1 <= abbr.length <= 10
# abbr consists of lowercase English letters and digits.
# All the integers in abbr will fit in a 32-bit integer.

from typing import List, Optional

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        return


class mySolution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # O(n), two-pointer, parse abbreviation and attempt to match to string
        # edge cases: no numbers in abbr, abbr is only numbers

        num = 0
        ptr = 0
        for i in range(len(abbr)):
            if ptr >= len(word) and i < len(abbr):
                return False

            ca = abbr[i]
            # process digit
            if ca.isdigit():
                num = (num * 10) + int(ca)
            else:
                # move pointer in word num spaces forward
                ptr += num

                # check if characters match
                if (ptr < len(word) and word[ptr] != abbr[i]) or ptr >= len(word):
                    return False

                # reset num, move ptr
                num = 0
                ptr += 1

        # handle abbr ending with a number
        # ptr should be num spaces from the end of word
        if num != (len(word) - ptr):
            return False

        return True


class testcase1:
    word = "internationalization"
    abbr = "i12iz4n"
    output = True

class testcase2:
    word = "apple"
    abbr = "a2e"
    output = False

class testcase3:
    word = "leetcoders"
    abbr = "10"
    output = True

class testcase4:
    word = "leetcoders"
    abbr = "11"
    output = False

class testcase5:
    word = "leetcoders"
    abbr = "leet11ers"
    output = False

class testcase6:
    word = "leetcoders"
    abbr = "leet"
    output = False

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.validWordAbbreviation(testcase1.word, testcase1.abbr)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.validWordAbbreviation(testcase2.word, testcase2.abbr)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.validWordAbbreviation(testcase3.word, testcase3.abbr)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.validWordAbbreviation(testcase4.word, testcase4.abbr)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = soln.validWordAbbreviation(testcase5.word, testcase5.abbr)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")

    # test example 6
    result6 = soln.validWordAbbreviation(testcase6.word, testcase6.abbr)
    print(f"Example 6 - Expected: {testcase6.output}, Got: {result6}, Correct: {result6 == testcase6.output}")