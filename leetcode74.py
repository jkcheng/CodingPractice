# 74. Search a 2D Matrix
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an m x n integer matrix matrix with the following two properties:
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List, Optional


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(logm): binary search for correct row
        row = None
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row = mid
                break
                # return search_row(matrix[row], target)
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        # return False if no row is found
        if row == None: return False

        # O(logn): binary search row for target
        rowarray = matrix[row]
        l, r = 0, len(rowarray) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == rowarray[mid]:
                return True
            elif target < rowarray[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False


class mySolution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search, search for the correct row, then search the row itself

        def search_row(array):
            l, r = 0, len(array) - 1
            while l <= r:
                mid = (l + r) // 2  # (l + (r-l))//2 to avoid overflow
                if target == array[mid]:
                    return True
                elif target < array[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            return False

        # binary search to find row
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2  # (l + (r-l))//2 to avoid overflow
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                # binary search this row
                return search_row(matrix[mid])
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        return False


class testcase1:
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    output = True

class testcase2:
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    output = False

class testcase3:
    matrix = [[60]]
    target = 60
    output = True

# ai generated
class testcase4:
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 1
    output = True

class testcase5:
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 10
    output = True


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.searchMatrix(testcase1.matrix, testcase1.target)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.searchMatrix(testcase2.matrix, testcase2.target)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.searchMatrix(testcase3.matrix, testcase3.target)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.searchMatrix(testcase4.matrix, testcase4.target)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")

    # test example 5
    result5 = soln.searchMatrix(testcase5.matrix, testcase5.target)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {testcase5.output == result5}")