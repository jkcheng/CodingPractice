# 530. Minimum Absolute Difference in BST
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:
#
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105
#
#
# Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # adapted from https://leetcode.com/problems/minimum-absolute-difference-in-bst/solutions/99905/two-solutions-in-order-traversal-and-a-more-general-way-using-treeset
        # use subfunction instead to avoid needing to recreate Solution instance
        def dfs(root: Optional[TreeNode], mindiff: float, prev: Optional[TreeNode]) -> float:
            if root is None:
                return mindiff, prev

            # process left subtree
            mindiff, prev = dfs(root.left, mindiff, prev)

            # calculate difference between current node val and previous node val
            if prev is not None:
                mindiff = min(mindiff, abs(root.val - prev.val))

            # set current node as previous
            prev = root

            # process right subtree
            mindiff, prev = dfs(root.right, mindiff, prev)

            return mindiff, prev

        mindiff, prev = dfs(root, float('inf'), None)
        return mindiff

class mySolution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # DFS, in-order traversal and compare difference between values adjacent
        # mindiff = 0

        inorder = []

        def dfs(root):
            if root.left is not None:
                dfs(root.left)

            inorder.append(root.val)

            if root.right is not None:
                dfs(root.right)

        dfs(root)

        # mindiff = float('inf')
        # prev = inorder[0]
        # for val in inorder[1:]:
        #     mindiff = min(mindiff, abs(val - prev))
        #     prev = val

        mindiff = min(abs(inorder[i] - inorder[i-1]) for i in range(1, len(inorder)))

        return mindiff

class testcase1:
    root = [4,2,6,1,3]
    output = 1
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [1,0,48,None,None,12,49]
    output = 1
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = [236,104,701,None,227,None,911]
    output = 9
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = Solution()

    # test example 1
    result1 = soln.getMinimumDifference(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.getMinimumDifference(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.getMinimumDifference(testcase3.rootnode)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )