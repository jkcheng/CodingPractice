# 1161. Maximum Level Sum of a Binary Tree
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
#
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
#
#
#
# Example 1:
#
#
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:
#
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# from collections import deque
def build_tree_queue(nodes: List[int]) -> Optional[TreeNode]:
    if len(nodes) == 0:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while len(queue) > 0:
        for _ in range(len(queue)):
            node = queue.pop(0) # use deque for optimal

            # add left child if present
            if i < len(nodes) and nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1

            # add right child if present
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1

    return root

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        return


class mySolution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # O(nodes), level order BFS
        queue = [root]  # use deque to optimize
        maxsum = float('-inf')
        maxlevel = 1

        # process nodes in queue level by level
        level = 1
        while len(queue) > 0:
            levelsum = 0
            # proceess nodes in current level
            for _ in range(len(queue)):
                node = queue.pop(0)
                # increment level sum
                levelsum += node.val

                # add children
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            # update max level
            if levelsum > maxsum:
                maxlevel = level
                maxsum = levelsum
            level += 1

        return maxlevel


from collections import deque
class mySolution_deque:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # O(nodes), level order BFS
        queue = deque([root])
        maxvalues = (float('-inf'), 0)

        # process nodes in queue level by level
        level = 1
        while len(queue) > 0:
            levelsum = 0
            # proceess nodes in current level
            for _ in range(len(queue)):
                node = queue.popleft()
                # increment level sum
                levelsum += node.val

                # add children
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            # update max level
            maxvalues = max(maxvalues, (levelsum, level), key=lambda x: x[0])
            level += 1

        return maxvalues[1]


class testcase1:
    root = [1, 7, 0, 7, -8, None, None]
    output = 2

class testcase2:
    root = [989, None, 10250, 98693, -89388, None, None, None, -32127]
    output = 2


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution_deque()

    # test example 1
    rootnode1 = build_tree_queue(testcase1.root)
    result1 = soln.maxLevelSum(rootnode1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    rootnode2 = build_tree_queue(testcase2.root)
    result2 = soln.maxLevelSum(rootnode2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")