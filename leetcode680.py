# 680. Valid Palindrome II
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#
#
#
# Example 1:
#
# Input: s = "aba"
# Output: true
# Example 2:
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
#
# Input: s = "abc"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.

from typing import List, Optional

# C++ recursive: https://leetcode.com/problems/valid-palindrome-ii/solutions/356505/c-concise-solution-by-kasracode-06ny
# python slicing: https://leetcode.com/problems/valid-palindrome-ii/solutions/107718/easy-to-understand-python-solution-by-ya-9ug6
class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True

class mySolution:
    def validPalindrome(self, s: str) -> bool:
        # O(n), two-pointer, start pointers at ends of string and check character equivalence
        # advance pointers if characters are the same, skip once if different

        def validate(l, r, s):
            while l <= r:
                if s[l] != s[r]:
                    return l, r, False

                l += 1
                r -= 1

            return l, r, True

        skipped = False
        firstl, firstr, firstoutcome = validate(0, len(s) - 1, s)

        if firstoutcome is False and skipped is False:
            skipped = True
            # skip left
            newl, newr, outcomel = validate(firstl + 1, firstr, s)

            # skip right
            newl2, newr2, outcomer = validate(firstl, firstr - 1, s)

            return outcomel or outcomer

        return firstoutcome

# more concise recursive function
class mySolution2:
    def validPalindrome(self, s: str) -> bool:
        # O(n), two-pointer, start pointers at ends of string and check character equivalence
        # advance pointers if characters are the same, skip once if different

        # recursive helper function
        def validate(l, r, s, skipped=False):
            while l <= r:
                if s[l] != s[r]:
                    if skipped is True:
                        return False
                    else:  # check skipping left and right
                        return validate(l + 1, r, s, True) or validate(l, r - 1, s, True)

                l += 1
                r -= 1

            return True

        return validate(0, len(s) - 1, s, False)


class testcase1:
    s = "aba"
    output = True

class testcase2:
    s = "abca"
    output = True

class testcase3:
    s = "abc"
    output = False

class testcase4:
    s = "aaabaacabaaa"
    output = True

class testcase5:
    s = "abccbca"
    output = True

class testcase6:
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    output = True


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.validPalindrome(testcase1.s)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.validPalindrome(testcase2.s)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.validPalindrome(testcase3.s)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.validPalindrome(testcase4.s)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = soln.validPalindrome(testcase5.s)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")

    # test example 6
    result6 = soln.validPalindrome(testcase6.s)
    print(f"Example 6 - Expected: {testcase6.output}, Got: {result6}, Correct: {result6 == testcase6.output}")