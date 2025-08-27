# 222. Count Complete Tree Nodes
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a complete binary tree, return the number of the nodes in the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Design an algorithm that runs in less than O(n) time complexity.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:
#
# Input: root = []
# Output: 0
# Example 3:
#
# Input: root = [1]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5 * 104].
# 0 <= Node.val <= 5 * 104
# The tree is guaranteed to be complete.

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_recursive(nodes: List[int], i: int, n: int) -> Optional[TreeNode]:
    root = None
    if i < n and nodes[i] is not None:
        root = TreeNode(nodes[i])
        root.left = build_tree_recursive(nodes, 2 * i + 1, n)
        root.right = build_tree_recursive(nodes, 2 * i + 2, n)
    return root


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        return


class mySolution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # recursive DFS, count nodes
        count = 0

        def dfs(root):
            nonlocal count
            if root is not None:
                count += 1
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return count

class testcase1:
    root = [1, 2, 3, 4, 5, 6]
    output = 6
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = []
    output = 0
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = [1]
    output = 1
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.countNodes(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.countNodes(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.countNodes(testcase3.rootnode)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )
