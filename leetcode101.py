# 101. Symmetric Tree
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
# Follow up: Could you solve it both recursively and iteratively?

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return


class mySolution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # dfs: compare left and right subtrees recursively
        # compare equivalent left/right nodes in each subtree to check if symmetric
        def dfs(left, right):
            # check if both are none
            if left is None and right is None:
                return True
            # check if only one is none
            elif left is None or right is None:
                return False
            # check if node values are different
            elif left.val != right.val:
                return False
            # both should be nodes win the same value
            # check if subtrees are symmetric
            else:
                return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root, root)

class testcase1:
    root = [1, 2, 2, 3, 4, 4, 3]
    output = True
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [1, 2, 2, None, 3, None, 3]
    output = False
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = [1, 2, 2, 3, 4, 4, None]
    output = False
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.isSymmetric(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.isSymmetric(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.isSymmetric(testcase3.rootnode)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )