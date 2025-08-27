# 100. Same Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
#
#
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_recursive(nodes: List[int], i: int, n: int) -> Optional[TreeNode]:
    root = None
    if len(nodes) == 0 or nodes is None:
        return root

    while i < n and nodes[i] is not None:
        # make TreeNode if value is available
        root = TreeNode(nodes[i])
        root.left = build_tree_recursive(nodes, 2 * i + 1, n)
        root.right = build_tree_recursive(nodes, 2 * i + 2, n)
        i += 1

    return root

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        if p != None and q != None:
            same = (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif (p == None and q != None) or (p != None and q == None):
            same = False

        return same

class mySolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # traverse both trees, check if output is equal at each step
        is_same = False

        if p is not None and q is not None and p.val == q.val:
            # is_same = all([self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)])
            is_same = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # set to true if both are none
        if p is None and q is None:
            is_same = True

        return is_same

class testcase1:
    p = [1, 2, 3]
    q = [1, 2, 3]
    output = True
    ptree = build_tree_recursive(p, 0, len(p))
    qtree = build_tree_recursive(q, 0, len(q))

class testcase2:
    p = [1, 2]
    q = [1, None, 2]
    output = False
    ptree = build_tree_recursive(p, 0, len(p))
    qtree = build_tree_recursive(q, 0, len(q))

class testcase3:
    p = [1, 2, 1]
    q = [1, 1, 2]
    output = False
    ptree = build_tree_recursive(p, 0, len(p))
    qtree = build_tree_recursive(q, 0, len(q))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.isSameTree(testcase1.ptree, testcase1.qtree)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.isSameTree(testcase2.ptree, testcase2.qtree)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.isSameTree(testcase3.ptree, testcase3.qtree)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )