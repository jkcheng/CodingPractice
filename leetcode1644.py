# 1644 - Lowest Common Ancestor of a Binary Tree II
# Posted on May 31, 2020 · 5 minute read
# Welcome to Subscribe On Youtube
#
# Formatted question description: https://leetcode.ca/all/1644.html
#
# 1644. Lowest Common Ancestor of a Binary Tree II
# Level
# Medium
#
# Description
# Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q.
# If either node p or q does not exist in the tree, return None. All values of the nodes in the tree are unique.
#
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as
# descendants (where we allow a node to be a descendant of itself)”.
# A descendant of a node x is a node y that is on the path from node x to some leaf node.
#
# Example 1:
#
# Image text
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#
# Output: 3
#
# Explanation: The LCA of nodes 5 and 1 is 3.
#
# Example 2:
#
# Image text
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#
# Output: 5
#
# Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.
#
# Example 3:
#
# Image text
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
#
# Output: null
#
# Explanation: Node 10 does not exist in the tree, so return null.
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 10^4].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q

# Follow up: Can you find the LCA traversing the tree, without checking nodes existence?

# tree setup
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mk_tree(nodes, i, n):
    root = None
    if (i < n) and nodes[i] is not None:
        root = TreeNode(nodes[i])
        root.left = mk_tree(nodes, 2 * i + 1, len(nodes))
        root.right = mk_tree(nodes, 2 * i + 2, len(nodes))
    return root


def prnt_tree(root):
    nodes = []
    q = [root]
    while any(q):
        node = q.pop(0)  # can use deque to optimize
        if node:
            nodes.append(node.val)
            if node.left or node.right or any(q):
                q.append(node.left)
                q.append(node.right)
        elif any(q):  # if node is None AND there's still stuff in q to process
            nodes.append('null')

    return nodes

def get_node_from_val(root, nodeval):
    def dfs(root):
        if root is None or root.val == nodeval:
            return root
        left, right = dfs(root.left), dfs(root.right)
        return left or right

    return dfs(root)

from typing import List


class Solution:
    def __init__(self):
        self.count = 0

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = self.lca(root, p, q)
        return res if self.count == 2 else None

    def lca(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None

        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)

        if root == p or root == q:
            self.count += 1
            return root

        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root

class mySolution:
    def __init__(self):
        self.found = 0

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root):
            # base case: leaf node
            if root is None:
                return root

            # explore children first before checking if p or q
            left, right = dfs(root.left), dfs(root.right)

            # increment found counter and return root if p or q encountered
            if root == p or root == q:
                self.found += 1
                return root

            # if p and q in left and right subtrees
            if left and right:
                return root
            return left or right

        ans = dfs(root)
        return ans if self.found == 2 else None

class testcase1:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 1
    rootnode = mk_tree(root, 0, len(root))
    pnode = get_node_from_val(rootnode, p)
    qnode = get_node_from_val(rootnode, q)

class testcase2:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 4
    rootnode = mk_tree(root, 0, len(root))
    pnode = get_node_from_val(rootnode, p)
    qnode = get_node_from_val(rootnode, q)

class testcase3:
    root = [1, 2]
    p = 1
    q = 2
    rootnode = mk_tree(root, 0, len(root))
    pnode = get_node_from_val(rootnode, p)
    qnode = get_node_from_val(rootnode, q)

# one node not in tree
class testcase4:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 10
    rootnode = mk_tree(root, 0, len(root))
    pnode = get_node_from_val(rootnode, p)
    qnode = TreeNode(q)

# both nodes not in tree
class testcase5:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 11
    q = 10
    rootnode = mk_tree(root, 0, len(root))
    pnode = TreeNode(p)
    qnode = TreeNode(q)