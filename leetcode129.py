# 129. Sum Root to Leaf Numbers
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:
#
#
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.

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


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        return

class mySolution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # DFS each path from root to leaf, build number + append to list
        # sum list
        # nums = []
        self.total = 0

        def dfs(root, num):
            if root is not None:
                num = 10 * num + root.val
                if root.left is not None:
                    dfs(root.left, num)
                if root.right is not None:
                    dfs(root.right, num)

                # add num to list if node is leaf node
                if root.left is None and root.right is None:
                    self.total += num

        dfs(root, 0)
        return self.total

class testcase1:
    root = [1, 2, 3]
    output = 25
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [4, 9, 0, 5, 1]
    output = 1026
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.sumNumbers(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.sumNumbers(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )