# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
# and postorder is the postorder traversal of the same tree, construct and return the binary tree.
#
#
#
# Example 1:
#
#
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
# Example 2:
#
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#
#
# Constraints:
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.

from typing import List,Optional


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

def tree_to_output(root: Optional[TreeNode]) -> List[int]:
    # todo
    return

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        return

class mySolution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # idea: last element in postorder will be root
        # find index value of root inside inorder, size of left subarray will be total left childern
        # right subarray will be total right children
        # use size of left and right subarrays to determine size of postorder subarrays for subproblems
        # recursively call buildTree using appropriate subarrays for the subtrees
        if len(postorder) == 0:
            return None

        rootval = postorder[-1]
        rootidx = inorder.index(rootval)
        size_right = (len(inorder) - 1) - rootidx

        root = TreeNode(rootval)
        root.left = self.buildTree(inorder[:rootidx], postorder[:rootidx])
        root.right = self.buildTree(inorder[rootidx + 1:], postorder[rootidx:rootidx + size_right])

        return root

class testcase1:
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    output = [3, 9, 20, None, None, 15, 7]

class testcase2:
    inorder = [-1]
    postorder = [-1]
    output = [-1]

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()
