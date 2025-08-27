# 54. Spiral Matrix
# Medium
# Topics
# Companies
# Hint
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        return


class mySolution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # track direction and boundary values
        # iterate through matrix indexes until reaching a boundary for the direction
        # change direction and update boundary to be one less than previous
        m = len(matrix)
        n = len(matrix[0])
        limits = [n - 1, m - 1, 0, 1]  # [top, down, bottom, up]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        i, j = 0, 0
        count = m * n
        seen = 0
        idx = 0
        ans = []
        while seen < count:
            # limit = limits[idx]
            # dir = dirs[idx]

            val = matrix[i][j]
            ans.append(val)

            # update direction
            if idx == 0 and j == limits[idx]:
                limits[idx] = limits[idx] - 1
                idx = idx + 1
            elif idx == 1 and i == limits[idx]:
                limits[idx] = limits[idx] - 1
                idx = idx + 1
            elif idx == 2 and j == limits[idx]:
                limits[idx] = limits[idx] + 1
                idx = idx + 1
            elif idx == 3 and i == limits[idx]:
                limits[idx] = limits[idx] + 1
                idx = 0

            # update indexes
            dir = dirs[idx]
            i += dir[0]
            j += dir[1]

            # increment seen
            seen += 1

        return ans

class testcase1:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

class testcase2:
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


