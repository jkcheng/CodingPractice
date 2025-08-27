# 73. Set Matrix Zeroes
# Medium
# Topics
# Companies
# Hint
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:
#
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
#
#
# Follow up:
#
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        return

# O(1) space: reuse first row and column as indicators whether the row or col has been written with zeroes
class mySolution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # iterate through matrix and flag rows/col to be zeroed
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                # set flag vars
                checkrow = matrix[i][0]
                checkcol = matrix[0][j]
                if val == 0:
                    # check if row needs to be zeroed
                    if checkrow != 'R' or checkrow != 'RC':
                        for l in range(n):
                            rowval = matrix[i][l]
                            if rowval == 0:
                                continue
                            if rowval == 'R' or rowval == 'RC':
                                continue
                            if rowval == 'C':
                                matrix[i][l] = 'RC'
                            else:
                                matrix[i][l] = 'R'
                    # check if col needs to be zeroed
                    if checkcol != 'C' or checkcol != 'RC':
                        for l in range(m):
                            colval = matrix[l][j]
                            if colval == 0:
                                continue
                            if colval == 'C' or colval == 'RC':
                                continue
                            if colval == 'R':
                                matrix[l][j] = 'RC'
                            else:
                                matrix[l][j] = 'C'

        # iterate through matrix and zero temporary values
        for i in range(m):
            for j in range(n):
                if matrix[i][j] in ('R', 'RC', 'C'):
                    matrix[i][j] = 0

        return matrix

# better O(1): check each value and flag row/col to be zeroed, then iterate through rows/cols again and zero
# need to store special boolean vars for matrix[0][0] because this value serves as both rol and col header
class mySolution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # iterate through matrix and flag rows/cols to zero
        m = len(matrix)
        n = len(matrix[0])

        firstrowzero, firstcolzero = False, False
        for i in range(m):
            for j in range(n):
                # flag row and col
                if matrix[i][j] == 0:
                    # special flags for first row/col
                    if i == 0:
                        firstrowzero = True
                    if j == 0:
                        firstcolzero = True
                    if i != 0 and j != 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        # iterate through matrix and zero non-header cells
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # zero first row
        if firstrowzero:
            for j in range(n):
                matrix[0][j] = 0

        # zero first col
        if firstcolzero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix

class testcase1:
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

class testcase2:
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

class testcase3:
    matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]