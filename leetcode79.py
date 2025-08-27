# 79. Word Search
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
# Constraints:
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
# Follow up: Could you use search pruning to make your solution faster with a larger board?

from typing import List,Optional

class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res


class mySolution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS, start search at each cell and check neighbors for next letter
        # continue until word found or next letter not in neighbors

        def dfs(i, j, k):
            # check for out of bounds
            if (i < 0) or (j < 0) or (i >= m) or (j >= n):
                return False

            # do nothing if current cell does not match letter in word
            if board[i][j] != word[k]:
                return False

            # return true if end of word reached
            if k == len(word) - 1:
                return True

            # mark as explored and explore neighbors
            curr_letter = board[i][j]
            board[i][j] = '#'
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            found = False
            for di, dj in neighbors:
                found = any([found, dfs(i + di, j + dj, k + 1)])

            # undo exploration mark
            board[i][j] = curr_letter

            return found

        m = len(board)
        n = len(board[0])
        found = False
        # optimization: check for frequency of start vs last letter in word in board
        # start searching using the lower frequency letter
        start_freq, end_freq = 0, 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start_freq += 1
                if board[i][j] == word[-1]:
                    end_freq += 1
        if end_freq < start_freq:
            word = word[::-1]

        for i in range(m):
            for j in range(n):
                found = any([found, dfs(i, j, 0)])
                if found:
                    return True

        return found


class testcase1:
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    output = True

class testcase2:
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    output = True

class testcase3:
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    output = False

# ai generated
class testcase4:
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABC"
    output = True

class testcase5:
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCE"
    output = True

class testcase6:
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ACE"
    output = False


if __name__ == "__main__":
    # Create solution instance
    solution = mySolution()

    # test example 1
    result1 = solution.exist(testcase1.board, testcase1.word)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = solution.exist(testcase2.board, testcase2.word)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = solution.exist(testcase3.board, testcase3.word)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = solution.exist(testcase4.board, testcase4.word)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    result5 = solution.exist(testcase5.board, testcase5.word)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")

    # test example 6
    result6 = solution.exist(testcase6.board, testcase6.word)
    print(f"Example 6 - Expected: {testcase6.output}, Got: {result6}, Correct: {result6 == testcase6.output}")