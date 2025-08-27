# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
# and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
#
#
# Example 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
# Constraints:
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def  build_tree_recursive(nodes: List[int], i: int, n: int) -> Optional[TreeNode]:
    root = None
    if i < n and nodes[i] is not None:
        root = TreeNode(nodes[i])
        root.left = build_tree_recursive(nodes, 2 * i + 1, n)
        root.right = build_tree_recursive(nodes, 2 * i + 2, n)
    return root

def tree_to_node_preorder(root: Optional[TreeNode]) -> List[int]:
    # todo
    return

# insight:
# inorder representation of tree is invariant
# when splitting the array on a given node, the left/right sections are themselves inorder representations of the left/right subtrees
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        rootval = preorder[0]
        rootidx = inorder.index(rootval)

        root = TreeNode(rootval)
        root.left = self.buildTree(preorder[1:rootidx + 1], inorder[:rootidx])
        root.right = self.buildTree(preorder[rootidx + 1:], inorder[rootidx + 1:])

        return root

# intuition:
# recursively build left and right subtrees
# key idea: use first value of preorder as root to find it's index position in inorder array
# use index position to split inorder and preorder arrays into left and right subtrees
class mySolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        rootval = preorder[0]
        rootidx = inorder.index(rootval)

        root = TreeNode(rootval)
        # left subtree values will be inorder[:rootidx], preorder[1:rootidx+1]
        root.left = self.buildTree(preorder[1:rootidx+1], inorder[:rootidx])
        # right subtree values will be inorder[rootidx+1:], preorder[rootidx+1:]
        root.right = self.buildTree(preorder[rootidx+1:], inorder[rootidx+1:])

        return root

class testcase1:
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

class testcase2:
    preorder = [-1]
    inorder = [-1]

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()
