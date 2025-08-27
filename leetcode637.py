# 637. Average of Levels in Binary Tree
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].
# Example 2:
#
#
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        return


class mySolution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # level order traversal
        ans = []
        queue = []  # use deque for more optimization

        if root is not None:
            queue.append(root)

        while len(queue) > 0:
            total = 0
            nodecount = 0
            for _ in range(len(queue)):
                node = queue.pop(0)
                total += node.val
                nodecount += 1
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            ans.append(total / nodecount)

        return ans

class testcase1:
    root = [3,9,20,None,None,15,7]
    output = [3.00000,14.50000,11.00000]
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [3,9,20,15,7]
    output = [3.00000,14.50000,11.00000]
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.averageOfLevels(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.averageOfLevels(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )