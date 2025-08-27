# 124. Binary Tree Maximum Path Sum
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        return

class mySolution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalmax = float('-inf')

        def depthSum(node: Optional[TreeNode]) -> TreeNode:
            max_sum = 0
            if node != None:
                lsum = max(depthSum(node.left), 0)
                rsum = max(depthSum(node.right), 0)

                max_sum = node.val + max(lsum, rsum)

                self.globalmax = max(self.globalmax, node.val + lsum + rsum)  # update global max

            return max_sum

        depthSum(root)
        return self.globalmax

class mySolution2:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS, check largest path sum that includes current node
        # update global max and recurse to children
        # return largest path sum
        self.total = float('-inf')

        # dfs
        def dfs(root):
            maxsum = 0
            if root is not None:
                maxleft = dfs(root.left)
                maxright = dfs(root.right)

                maxsum = max(root.val, root.val + maxleft, root.val + maxright)

                # check if current node serves as root for global path max
                self.total = max(self.total, root.val + maxleft + maxright, root.val, root.val + maxleft,
                                 root.val + maxright)

            return maxsum

        dfs(root)
        return self.total

class testcase1:
    root = [1, 2, 3]
    output = 6
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [-10, 9, 20, None, None, 15, 7]
    output = 42
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.maxPathSum(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.maxPathSum(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")