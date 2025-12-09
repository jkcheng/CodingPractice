# 872. Leaf-Similar Trees
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
#
#
# Example 1:
#
#
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
# Example 2:
#
#
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_recursive(nodes: List[int], i: int, n: int) -> Optional[TreeNode]:
    if i >= n or nodes[i] is None:
        return None

    root = TreeNode(nodes[i])
    root.left = build_tree_recursive(nodes, 2*i + 1, len(nodes))
    root.right = build_tree_recursive(nodes, 2*i + 2, len(nodes))

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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.iterative(root1, []) == self.iterative(root2, [])

    def iterative(self, root, s):
        if root is not None:
            stack = []
            stack.append(root)
            while stack:
                x = stack.pop(-1)
                if x.left is None and x.right is None:
                    s.append(x.val)
                    continue
                if x.right is not None:
                    stack.append(x.right)
                if x.left is not None:
                    stack.append(x.left)
        return s

class mySolution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode], leafs: List[int]) -> List[int]:
            if root is None:
                return leafs

            if root.left is None and root.right is None:
                leafs.append(root.val)
                return leafs

            leafs = dfs(root.left, leafs)
            leafs = dfs(root.right, leafs)

            return leafs

        leafs1 = dfs(root1, [])
        leafs2 = dfs(root2, [])

        return leafs1 == leafs2

class testcase1:
    root1 = [3,5,1,6,2,9,8,None,None,7,4]
    # root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    output = True

class testcase2:
    root1 = [1, 2, 3]
    root2 = [1, 3, 2]
    output = False


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    rootnode1_1 = build_tree_queue(testcase1.root1)
    rootnode1_2 = build_tree_queue(testcase1.root2)
    result1 = soln.leafSimilar(rootnode1_1, rootnode1_2)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    rootnode2_1 = build_tree_queue(testcase2.root1)
    rootnode2_2 = build_tree_queue(testcase2.root2)
    result2 = soln.leafSimilar(rootnode2_1, rootnode2_2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")


