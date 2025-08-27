# 102. Binary Tree Level Order Traversal
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
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
# -1000 <= Node.val <= 1000

from typing import List, Optional

# BFS implementation using a single deque for optimization
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


from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        ans = []
        while len(queue) > 0:
            queuelength = len(queue)
            level = []
            for i in range(queuelength):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if len(level) > 0:
                ans.append(level)

        return ans

class mySolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traversal
        # add nodes to queue, process each node
        # add node values to ans and children to queue
        ans = []
        queue = []  # can use deque and .popleft() for optimization

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

            ans.append(level)

        return ans

class testcase1:
    root = [3, 9, 20, None, None, 15, 7]
    output = [[3], [9, 20], [15, 7]]
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = [1]
    output = [[1]]
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase3:
    root = []
    output = []
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase4:
    root = [1,2,3,4,5,6,7,8,9,10]
    output = [[1],[2,3],[4,5,6,7],[8,9,10]]
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.levelOrder(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.levelOrder(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.levelOrder(testcase3.rootnode)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )

    # test example 4
    result4 = soln.levelOrder(testcase4.rootnode)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}" )