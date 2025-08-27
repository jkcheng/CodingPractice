# 236. Lowest Common Ancestor of a Binary Tree
# Solved
# Medium
# Topics
# Companies
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:
#
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

from typing import List


# tree practice
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



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root is None or root == p or root == q:
                return root
            left, right = dfs(root.left), dfs(root.right)
            if left and right:
                return root
            return left or right

        return dfs(root)

class mySolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root is None or root == p or root == q:
                return root
            left, right = dfs(root.left), dfs(root.right)
            # if both p and q in subtree, then return root as LCA
            if left and right:
                return root

            return left or right

        return dfs(root)

# followup: p or q may not be in tree, not checking existence of p or q first
# use post-order traversal to note if p and q found
class Solution_followup:
    def __init__(self):
        self.count = 0

    def lca(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None

        # explore first before returning to properly count found nodes
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

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = self.lca(root, p, q)
        return res if self.count == 2 else None



class mySolution_followup:
    def __init__(self):
        self.count = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root is None:
                return None

            # explore first to properly count nodes
            left, right = dfs(root.left), dfs(root.right)

            # behavior change: update count of nodes found when p or q encountered
            if root == p or root == q:
                self.count += 1
                return root

            # if both p and q in subtree, then return root as LCA
            if left and right:
                return root
            return left or right

        ans = dfs(root)
        return ans if self.count == 2 else None

class testcase1:
    # leetcode input display
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

class testcase4:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 9
    q = 1
    rootnode = mk_tree(root, 0, len(root))
    # special error case where node not in tree
    pnode = TreeNode(p)
    qnode = get_node_from_val(rootnode, q)

    # expected: return node q

class testcase5:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 9
    q = 10
    rootnode = mk_tree(root, 0, len(root))
    # special error case where both nodes not in tree
    pnode = TreeNode(p)
    qnode = TreeNode(q)

    # expected: null