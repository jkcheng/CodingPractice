# 98. Validate Binary Search Tree
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive DFS version (complicated!)
        def minMaxDFS(node):
            # base case
            if node == None:
                is_valid = True
                minval = float("inf")
                maxval = -float("inf")
            else:
                left_isvalid, left_minval, left_maxval = minMaxDFS(node.left)
                right_isvalid, right_minval, right_maxval = minMaxDFS(node.right)
                if left_isvalid and right_isvalid and (node.val > left_maxval) and (node.val < right_minval):
                    is_valid = True
                else:
                    is_valid = False

                minval = min(node.val, left_minval)
                maxval = max(node.val, right_maxval)

            return (is_valid, minval, maxval)

        return minMaxDFS(root)[0]

class mySolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in-order traversal of BST has increasing values
        # store nodes in-order in list and check if list is increasing

        nodevals = []
        def inorder(root):
            if root.left is not None:
                inorder(root.left)
            nodevals.append(root.val)
            if root.right is not None:
                inorder(root.right)

        inorder(root)
        prev = float('-inf')
        for n in nodevals:
            if n <= prev:
                return False
            prev = n

        return True

class mySolution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in-order traversal using stack and pointer

        stack = []
        prev = None
        while len(stack) > 0  or root is not None:
            # recurse down left subtree
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            # check of root is smaller than prev val
            if prev is not None and root.val <= prev.val:
                return False

            prev = root
            root = root.right

        return True

class testcase1:
    root = [2,1,3]
    output = True
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [5,1,4,None,None,3,6]
    output = False
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = [1]
    output = True
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.isValidBST(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.isValidBST(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.isValidBST(testcase3.rootnode)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )