# 230. Kth Smallest Element in a BST
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
#
#
# Example 1:
#
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
#
# Constraints:
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
#
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

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

# inorder traversal, iterative with stack
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        order = []
        node = root.left

        while stack or node:
            while node != None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            order.append(node.val)
            # exit early to output kth result if found
            k -= 1
            if k == 0:
                return node.val

            # set pointer to right child for next iteration of loop
            node = node.right

        return order


class mySolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # using nonlocal variables outside recursive function

        # in-order traversal
        ans = None
        def dfs(root):
            nonlocal k
            nonlocal ans

            if root.left is not None:
                dfs(root.left)

            k -= 1
            if k == 0:
                ans = root.val
                return

            if root.right is not None:
                dfs(root.right)

        dfs(root)
        return ans

class mySolution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # tracking node values in list with early termination

        # in-order traversal
        nodevals = []
        def dfs(root):
            if root.left is not None:
                dfs(root.left)

            # terminate early to avoid traversing entire tree
            # check needs to be here before appending root.val to list
            if len(nodevals) == k:
                return
            nodevals.append(root.val)

            if root.right is not None:
                dfs(root.right)

        dfs(root)
        return nodevals[-1]


class testcase1:
    root = [3, 1, 4, None, 2]
    k = 1
    output = 1
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [5, 3, 6, 2, 4, None, None, 1]
    k = 3
    output = 3
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = [1]
    k = 1
    output = 1
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.kthSmallest(testcase1.rootnode, testcase1.k)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.kthSmallest(testcase2.rootnode, testcase2.k)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.kthSmallest(testcase3.rootnode, testcase3.k)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")
