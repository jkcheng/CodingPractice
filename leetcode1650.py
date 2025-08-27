# 1650. Lowest Common Ancestor of a Binary Tree III
# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
#
# Each node will have a reference to its parent node. The definition for Node is below:
#
# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia:
# "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as
# descendants (where we allow a node to be a descendant of itself)."
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
# Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
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
# p and q exist in the tree.

# tree setup
class TreeNodeWithParent:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def mk_tree_with_parent(nodes, i, n, parent=None):
    root = None
    if (i < n) and nodes[i] is not None:
        root = TreeNodeWithParent(nodes[i])
        root.left = mk_tree_with_parent(nodes, 2 * i + 1, len(nodes), root)
        root.right = mk_tree_with_parent(nodes, 2 * i + 2, len(nodes), root)
        root.parent = parent
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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # O(h) two pointer optimized
        a, b = p, q
        while a != b:
            a = a.parent if a.parent else q
            b = b.parent if b.parent else p
        return


class mySolution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # O(h) time, O(h) space: create set of nodes seen and check if parent has been seen before
        seen = set()

        # traverse upward from p
        while p is not None:
            seen.add(p)
            p = p.parent

        # traverse upward from q and first parent previously encountered is LCA
        while q is not None:
            if q in seen:
                return q
            q = q.parent

        return None

class mySolution2:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # O(h) time, O(1) space: traverse upward until root, then count number of steps lower node needs to reach root for depth diff
        # restart and traverse upward from lower node depth diff steps, then traverse upward simultaneously
        # LCA is when pointers reach same node

        # use a,b for traversal
        a, b = p, q
        # traverse upward from p
        psteps = 0
        while a is not None:
            a = a.parent
            # only count steps to another node
            if a is not None:
                psteps += 1

        # traverse upward from q and first parent previously encountered is LCA
        qsteps = 0
        while b is not None:
            b = b.parent
            # only count steps to another node
            if b is not None:
                qsteps += 1

        # make sure psteps is larger
        if qsteps > psteps:
            psteps, qsteps = qsteps, psteps
            a, b = q, p # q is lower
        else:
            a, b = p, q # p is lower
        delta = psteps-qsteps

        # traverse upward again delta steps
        while a is not None and delta > 0:
            a = a.parent
            delta -= 1

        while a != b:
            a = a.parent
            b = b.parent

        return a

class mySolution3:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # O(h) time, O(1) space: traverse upward until root, then count number of steps lower node needs to reach root for depth diff
        # restart and traverse upward from lower node depth diff steps, then traverse upward simultaneously
        # LCA is when pointers reach same node

        a, b = p, q
        while a.parent is not None and b.parent is not None:
            a = a.parent
            b = b.parent

        # count delta
        delta = 0
        if a.parent is None:
            higher, lower = p, q
            while b.parent is not None:
                b = b.parent
                delta += 1
        else:
            higher, lower = q, p
            while a.parent is not None:
                a = a.parent
                delta += 1

        while lower != higher:
            if delta > 0:
                delta -= 1
                lower = lower.parent
            else:
                lower = lower.parent
                higher = higher.parent

        return higher






class testcase1:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 1
    rootnode = mk_tree_with_parent(root, 0, len(root))
    pnode = get_node_from_val(rootnode, p)
    qnode = get_node_from_val(rootnode, q)

class testcase2:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 4
    rootnode = mk_tree_with_parent(root, 0, len(root))
    pnode = get_node_from_val(rootnode, p)
    qnode = get_node_from_val(rootnode, q)

class testcase3:
    root = [1, 2]
    p = 1
    q = 2
    rootnode = mk_tree_with_parent(root, 0, len(root))
    pnode = get_node_from_val(rootnode, p)
    qnode = get_node_from_val(rootnode, q)

# missing nodes, violates requirements
class testcase4:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 10
    rootnode = mk_tree_with_parent(root, 0, len(root))
    pnode = get_node_from_val(rootnode, p)
    qnode = TreeNodeWithParent(q)

# missing nodes, violates requirements
class testcase5:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 11
    q = 10
    rootnode = mk_tree_with_parent(root, 0, len(root))
    pnode = TreeNodeWithParent(p)
    qnode = TreeNodeWithParent(q)

