# 1676. Lowest Common Ancestor of a Binary Tree IV
# Description
# Given the root of a binary tree and an array of TreeNode objects nodes, return the lowest common ancestor (LCA) of all the nodes in nodes. All the nodes will exist in the tree, and all values of the tree's nodes are unique.
#
# Extending the definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn in a binary tree T is the lowest node that has every pi as a descendant (where we allow a node to be a descendant of itself) for every valid i". A descendant of a node x is a node y that is on the path from node x to some leaf node.
#
#
#
# Example 1:
#
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
# Output: 2
# Explanation: The lowest common ancestor of nodes 4 and 7 is node 2.
# Example 2:
#
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
# Output: 1
# Explanation: The lowest common ancestor of a single node is the node itself.
#
# Example 3:
#
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
# Output: 5
# Explanation: The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -109 <= Node.val <= 109
# All Node.val are unique.
# All nodes[i] will exist in the tree.
# All nodes[i] are distinct.

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
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        return


class mySolution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        return

class testcase1:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    nodes = [4, 7]
    rootnode = mk_tree(root, 0, len(root))
    nodelist = [get_node_from_val(rootnode, n) for n in nodes]

class testcase2:
    root = [3,5,1,6,2,0,8,None,None,7,4]
    nodes = [1]
    rootnode = mk_tree(root, 0, len(root))
    nodelist = [get_node_from_val(rootnode, n) for n in nodes]


class testcase3:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    nodes = [7, 6, 2, 4]
    rootnode = mk_tree(root, 0, len(root))
    nodelist = [get_node_from_val(rootnode, n) for n in nodes]

# one node not in tree
# class testcase4:
#     root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
#     p = 5
#     q = 10
#     rootnode = mk_tree(root, 0, len(root))
#     pnode = get_node_from_val(rootnode, p)
#     qnode = TreeNode(q)
#
# # both nodes not in tree
# class testcase5:
#     root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
#     p = 11
#     q = 10
#     rootnode = mk_tree(root, 0, len(root))
#     pnode = TreeNode(p)
#     qnode = TreeNode(q)

