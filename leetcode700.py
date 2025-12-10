# 700. Search in a Binary Search Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
#
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:
#
#
# Input: root = [4,2,7,1,3], val = 5
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def build_tree_queue(nodes: List[int]) -> Optional[TreeNode]:
    if len(nodes) == 0:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while len(queue) > 0:
        for _ in range(len(queue)):
            # node = queue.pop(0)
            node = queue.popleft()

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

from collections import deque
def print_tree(root: Optional[TreeNode]) -> List[int]:
    output = []
    if root is None:
        return output

    queue = deque([root])
    while len(queue) > 0:
        for _ in range(len(queue)):
            # node = queue.pop(0)
            node = queue.popleft()
            output.append(node.val)

            # add both children if any are present, skip if both are None
            if node.left is not None or node.right is not None:
                queue.append(node.left)
                queue.append(node.right)

    # replace None with 'null' to match leetcode output
    return [val if val is not None else 'null' for val in output]

# https://leetcode.com/problems/search-in-a-binary-search-tree/solutions/147001/python-solution-iterative-o1-space-on-lo-ihta
class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        current_node = root
        while current_node != None:
            if current_node.val == val:
                return current_node
            elif current_node.val < val:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return None


class mySolution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # O(logn), recursively traverse left/right child of node if smaller/larger
        # return node when found else null

        while root is not None:
            if val == root.val:
                return root
            elif val < root.val:
                return self.searchBST(root.left, val)
            else:
                return self.searchBST(root.right, val)

        return None

class mySolution_iterative:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # O(logn), iterative, reassign root instead of recursive function calls

        while root is not None:
            if val == root.val:
                return root
            elif val < root.val:
                root = root.left # reassign root
            else:
                root = root.right

        return root


class testcase1:
    root = [4, 2, 7, 1, 3]
    val = 2
    output = [2, 1, 3]

class testcase2:
    root = [4, 2, 7, 1, 3]
    val = 5
    output = []


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution_iterative()

    # test example 1
    rootnode1 = build_tree_queue(testcase1.root)
    result1 = soln.searchBST(rootnode1, testcase1.val)
    listresult1 = print_tree(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    rootnode2 = build_tree_queue(testcase2.root)
    result2 = soln.searchBST(rootnode2, testcase2.val)
    listresult2 = print_tree(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")