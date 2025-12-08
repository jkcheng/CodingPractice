# 199. Binary Tree Right Side View
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
#
#
# Example 1:
#
# Input: root = [1,2,3,null,5,null,4]
#
# Output: [1,3,4]
#
# Explanation:
#
#
#
# Example 2:
#
# Input: root = [1,2,3,4,null,null,null,5]
#
# Output: [1,3,4,5]
#
# Explanation:
#
#
#
# Example 3:
#
# Input: root = [1,null,3]
#
# Output: [1,3]
#
# Example 4:
#
# Input: root = []
#
# Output: []
#
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
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

def build_tree_queue(nodes: List[int]) -> Optional[TreeNode]:
    if len(nodes) == 0:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while len(queue) > 0:
        for _ in range(len(queue)):
            node = queue.pop(0)

            # add left child
            if i < len(nodes) and nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1

            # add right child
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1

    return root


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal
        ans = []
        queue = [root]  # use deque for more efficiency

        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            # add rightmost node of level to ans
            if len(level) > 0:
                ans.append(level[-1])

        return ans

from collections import deque # use deque for optimized queue
class mySolution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # O(nodes), BFS level order traversal
        # add nodes to queue, add last node of each level to result set
        output = []
        if root is None:
            return output

        queue = [root]  # use deque for optimal

        # process nodes level by level
        while len(queue) > 0:
            # add rightmost node to output
            output.append(queue[-1].val)

            # process nodes in level
            for _ in range(len(queue)):
                node = queue.pop(0)
                # add child nodes to queue
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return output

class testcase1:
    root = [1,2,3,None,5,None,4]
    output = [1,3,4]

class testcase2:
    root = [1,2,3,4,None,None,None,5]
    output = [1,3,4,5]

class testcase3:
    root = [1,None,3]
    output = [1,3]

class testcase4:
    root = []
    output = []


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    rootnode1 = build_tree_queue(testcase1.root)
    result1 = soln.rightSideView(rootnode1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    rootnode2 = build_tree_queue(testcase2.root)
    result2 = soln.rightSideView(rootnode2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    rootnode3 = build_tree_queue(testcase3.root)
    result3 = soln.rightSideView(rootnode3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )

    # test example 4
    rootnode4 = build_tree_queue(testcase4.root)
    result4 = soln.rightSideView(rootnode4)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}" )