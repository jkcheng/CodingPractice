# 17. Letter Combinations of a Phone Number
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from typing import List,Optional

# more concise code backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []

        def backtrack(letters, i):
            if i >= len(digits):
                if letters != '':
                    ans.append(letters)
                return

            d = digits[i]
            for c in digits_to_letters[d]:
                backtrack(letters + c, i + 1)

            return

        letters = ''
        backtrack(letters, 0)
        return ans

class mySolution:
    def letterCombinations(self, digits: str) -> List[str]:
        # create mapping of digits -> letters and loop through every combination?
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # use a recursive helper function similar to dfs approaches
        def explore(i, combination):
            if i >= len(digits):
                if combination != '':
                    ans.append(combination)
            else:
                num = digits[i]
                letters = mapping[num]
                for letter in letters:
                    explore(i + 1, combination + letter)

        ans = []
        explore(0, '')

        return ans


class testcase1:
    digits = "23"
    output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]

class testcase2:
    digits = ""
    output = []

class testcase3:
    digits = "2"
    output = ["a","b","c"]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.letterCombinations(testcase1.digits)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.letterCombinations(testcase2.digits)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.letterCombinations(testcase3.digits)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")