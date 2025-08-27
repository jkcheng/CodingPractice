# 212. Word Search II
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#
#
# Example 1:
#
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
# Constraints:
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 104
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

from typing import List,Optional

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            dic_to_search = root.children
            if symbol not in dic_to_search:
                dic_to_search[symbol] = TrieNode()
            root.children = dic_to_search
            root = root.children[symbol]
        root.end_node = 1

class Solution:
    def findWords(self, board, words):
        self.num_words = len(words)
        res, trie = [], Trie()
        for word in words: trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if self.num_words == 0: return

        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return
        tmp = board[i][j]
        if tmp not in node.children: return

        board[i][j] = "#"
        for x,y in [[0,-1], [0,1], [1,0], [-1,0]]:
            self.dfs(board, node.children[tmp], i+x, j+y, path+tmp, res)
        board[i][j] = tmp


class mySolution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # DFS + trie: build a trie of chars in words
        # dfs in all directions starting from each square in board
        # check if string formed by dfs path is in trie

        # build trie from words
        word_trie = {}
        for word in words:
            table = word_trie
            for c in word:
                table[c] = table.get(c, {})
                table = table[c]

            # add ending char
            table['#'] = {}

        # dfs explore board
        m = len(board)
        n = len(board[0])

        def dfs(i, j, board, table, candidate) -> None:
            # check if out of bounds
            if (i >= m) or (j >= n) or (i < 0) or (j < 0):
                return  # [None] # ?

            c = board[i][j]
            # if current char not next letter in trie
            if c not in table:
                return  # [None] # ?

            # add current char to candidate str
            candidate += c
            # add candidate to ans if c is end char
            if '#' in table[c]:
                ans.add(candidate)

            # mark c as explored and explore neighbors
            board[i][j] = '.'
            neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in neighbors:
                dfs(i + di, j + dj, board, table[c], candidate)

            # reset to original c after exploring
            board[i][j] = c

        ans = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, board, word_trie, '')

        return list(ans)

class testcase1:
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    output = ["eat","oath"]

class testcase2:
    board = [["a","b"],["c","d"]]
    words = ["abcb"]
    output = []

class testcase3:
    board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
    words = ["oa","oaa"]
    output = ["oa","oaa"]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.findWords(testcase1.board, testcase1.words)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.findWords(testcase2.board, testcase2.words)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.findWords(testcase3.board, testcase3.words)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")