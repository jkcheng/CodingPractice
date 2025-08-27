# 114. Flatten Binary Tree to Linked List
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the root of a binary tree, flatten the tree into a "linked list":
#
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
#
#
# Example 1:
#
#
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
#
#
# Follow up: Can you flatten the tree in-place (with O(1) extra space)?

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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """


class mySolution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # recursively preorder traverse tree
        # set left child to none, right child to preorder traversal result

        # traversal only
        nodes = []

        def preorder_traverse(root):
            if root is not None:
                nodes.append(root)
                if root.left is not None:
                    preorder_traverse(root.left)
                if root.right is not None:
                    preorder_traverse(root.right)

        preorder_traverse(root)

        # reconnect nodes as list
        dummy = TreeNode(-1)
        prev = dummy
        for node in nodes:
            prev.left = None
            prev.right = node
            prev = node

        prev.right = None

class testcase1:
    root = [1, 2, 5, 3, 4, None, 6]
    output = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = []
    output = []
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = [0]
    output = [0]
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    soln.flatten(testcase1.rootnode)

    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}")