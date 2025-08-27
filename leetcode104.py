# 104. Maximum Depth of Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:
#
# Input: root = [1,null,2]
# Output: 2
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_recursive(nodes: List[int], i: int, n: int) -> Optional[TreeNode]:
    root = None # default return value if i is out of bounds

    if i < n and nodes[i] is not None:
        # make TreeNode if value is available
        root = TreeNode(nodes[i])
        root.left = build_tree_recursive(nodes, 2 * i + 1, n)
        root.right = build_tree_recursive(nodes, 2 * i + 2, n)

    return root


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return

class mySolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if root is None:
                return depth

            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)

class testcase1:
    root = [3, 9, 20, None, None, 15, 7]
    output = 3
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [1, None, 2]
    output = 2
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = []
    output = 0
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.maxDepth(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.maxDepth(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.maxDepth(testcase3.rootnode)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )

