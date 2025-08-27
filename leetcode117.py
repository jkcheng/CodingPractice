# 117. Populating Next Right Pointers in Each Node II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a binary tree
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node,
# the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100
#
#
# Follow-up:
#
# You may only use constant extra space.
# The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

from typing import List, Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def build_tree_recursive(nodes: List[int], i: int, n: int) -> Optional[Node]:
    root = None
    if i < n and nodes[i] is not None:
        root = Node(nodes[i])
        root.left = build_tree_recursive(nodes, 2 * i + 1, n)
        root.right = build_tree_recursive(nodes, 2 * i + 2, n)

    return root

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        return


class mySolution:
    def connect(self, root: 'Node') -> 'Node':
        # organize nodes into level order traversal
        # set next pointer to next node in level order
        if root == None:
            return root

        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            levelcount = len(queue)
            # loop through levelcount number of items
            for i in range(levelcount):
                node = queue.popleft()
                # node.next is next node in queue if not last node of level
                if i == levelcount-1:
                    node.next = None
                else:
                    node.next = queue[0]
                # add children to queue
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return root


class testcase1:
    root = [1, 2, 3, 4, 5, None, 7]
    output = [1, None, 2, 3, None, 4, 5, 7, None]
    rootnode = build_tree_recursive(root, 0, len(root))

class testcase2:
    root = []
    output = []
    rootnode = build_tree_recursive(root, 0, len(root))

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.connect(testcase1.rootnode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.connect(testcase2.rootnode)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

