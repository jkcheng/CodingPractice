# 112. Path Sum
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
#
#
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There are two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
# Example 3:
#
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        return

class mySolution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # recursion, DFS
        # pathsum = 0

        def dfs(root, cursum):
            if root is not None:
                cursum += root.val

                # if cursum == targetSum:
                #     return True

                if root.left:
                    left = dfs(root.left, cursum)
                else:
                    left = False
                if root.right:
                    right = dfs(root.right, cursum)
                else:
                    right = False

                if root.left is None and root.right is None:
                    return cursum == targetSum
                else:
                    return left or right

            return cursum == targetSum

            #     # return dfs(root.left, cursum) or dfs(root.right, cursum)
            # else:
            #     return cursum == targetSum

        return dfs(root, 0) if root is not None else False

class testcase1:
    root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    targetSum = 22
    output = True
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [1, 2, 3]
    targetSum = 5
    output = False
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = []
    targetSum = 0
    output = False
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.hasPathSum(testcase1.rootnode, testcase1.targetSum)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.hasPathSum(testcase2.rootnode, testcase2.targetSum)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.hasPathSum(testcase3.rootnode, testcase3.targetSum)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )
