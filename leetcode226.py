# 226. Invert Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, invert the tree, and return its root.
#
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

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

def tree_to_node_list(root: Optional[TreeNode]) -> List[int]:
    # todo
    return

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

class mySolution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursively swap left/right nodes
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

class testcase1:
    root = [4, 2, 7, 1, 3, 6, 9]
    output = [4, 7, 2, 9, 6, 3, 1]
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [2, 1, 3]
    output = [2, 3, 1]
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = []
    output = []
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.invertTree(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.invertTree(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.invertTree(testcase3.rootnode)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")
