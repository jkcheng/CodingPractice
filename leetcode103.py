# 103. Binary Tree Zigzag Level Order Traversal
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

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
    def zigzagLevelOrder(self, root):
        if not root: return []
        queue = deque([root])
        result, direction = [], 1

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level[::direction])
            direction *= (-1)
        return result

class mySolution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traversal
        # use queue, process each node of current level from queue
        # add node val to ans, add children to queue
        queue = []  # use deque for optimization
        ans = []
        reverse = False

        if root is not None:
            queue.append(root)

        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            if reverse:
                ans.append(level[::-1])
                reverse = False
            else:
                ans.append(level)
                reverse = True

        return ans

class testcase1:
    root = [3,9,20,None,None,15,7]
    output = [[3],[20,9],[15,7]]
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [1]
    output = [[1]]
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = []
    output = []
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.zigzagLevelOrder(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.zigzagLevelOrder(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.zigzagLevelOrder(testcase3.rootnode)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )