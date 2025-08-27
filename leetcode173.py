# 173. Binary Search Tree Iterator
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#
# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
# int next() Moves the pointer to the right, then returns the number at the pointer.
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
#
# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
#
#
#
# Example 1:
#
#
# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]
#
# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 105].
# 0 <= Node.val <= 106
# At most 105 calls will be made to hasNext, and next.
#
#
# Follow up:
#
# Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

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


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):

    def next(self) -> int:
        return

    def hasNext(self) -> bool:
        return


class myBSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # traverse left child until leaf node to get smallest node in tree
        # add nodes seen during traversal to stack
        self.stack = []
        while root is not None:
            self.stack.append(root)
            root = root.left

        self.curnode = TreeNode(-1)

    def next(self) -> int:
        # recursively traverse left children of the RIGHT subtree
        # add nodes seen during traversal to stack
        # if leaf node, then pop the top node off of stack for next
        if self.curnode.right is not None:
            self.curnode = self.curnode.right
            while self.curnode.left is not None:
                self.stack.append(self.curnode)
                self.curnode = self.curnode.left
            return self.curnode.val
        else:
            self.curnode = self.stack.pop()
            return self.curnode.val

    def hasNext(self) -> bool:
        # check if any right subtree or nodes in stack
        # return False if both are false
        return self.curnode.right is not None or len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class testcase1:
    input = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    inputvals = [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]
    output = [None, 3, 7, True, 9, True, 15, True, 20, True]
    