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

from typing import List, Optional


# tree practice
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree_queue(nodes: List[int]) -> Optional[TreeNode]:
    if len(nodes) == 0:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    n = len(nodes)
    while len(queue) > 0:
        for _ in range(len(queue)):
            node = queue.pop(0)
            # add left child
            if i < n and nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1

            # add right child
            if i < n and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1

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

def get_node_from_val(root, nodeval, create=False):
    def dfs(root):
        if root is None or root.val == nodeval:
            return root
        left, right = dfs(root.left), dfs(root.right)
        return left or right

    result = dfs(root)
    return result if (not create and result) else TreeNode(nodeval)



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

class mySolution_self:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # O(height), dfs to find p and q, return lowest node where p and q are children in separate subtrees
        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # return lca if p and q are found in left and right subtrees
        if left is not None and right is not None:
            return root

        return left or right

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
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 1
    output = 3

class testcase2:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 5
    q = 4
    output = 5

class testcase3:
    root = [1, 2]
    p = 1
    q = 2
    output = 1

# test case for followup: p or q not in tree
class testcase4:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 9
    q = 1
    # expected: return None or node q if default solution is used as-is
    output = None

# test case for followup: p and q both not in tree
class testcase5:
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    p = 9
    q = 10
    # expected: null
    output = None


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution_self()

    # test example 1
    rootnode1 = build_tree_queue(testcase1.root)
    p1 = get_node_from_val(rootnode1, testcase1.p)
    q1 = get_node_from_val(rootnode1, testcase1.q)
    result1 = soln.lowestCommonAncestor(rootnode1, p1, q1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1.val}, Correct: {result1.val == testcase1.output}")

    # test example 2
    rootnode2 = build_tree_queue(testcase2.root)
    p2 = get_node_from_val(rootnode2, testcase2.p)
    q2 = get_node_from_val(rootnode2, testcase2.q)
    result2 = soln.lowestCommonAncestor(rootnode2, p2, q2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2.val}, Correct: {result2.val == testcase2.output}")

    # test example 3
    rootnode3 = build_tree_queue(testcase3.root)
    p3 = get_node_from_val(rootnode3, testcase3.p)
    q3 = get_node_from_val(rootnode3, testcase3.q)
    result3 = soln.lowestCommonAncestor(rootnode3, p3, q3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3.val}, Correct: {result3.val == testcase3.output}")

    # create Solution instance for followup tests
    soln = mySolution_followup()

    # test example 4 for followup: p or q not in tree
    rootnode4 = build_tree_queue(testcase4.root)
    p4 = get_node_from_val(rootnode4, testcase4.p) # not in tree
    q4 = get_node_from_val(rootnode4, testcase4.q)
    result4 = soln.lowestCommonAncestor(rootnode4, p4, q4)
    if result4 is None:
        result4 = TreeNode(None)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4.val}, Correct: {result4.val == testcase4.output}")

    # test example 5 for followup: p and q not in tree
    rootnode5 = build_tree_queue(testcase5.root)
    p5 = get_node_from_val(rootnode5, testcase5.p)
    q5 = get_node_from_val(rootnode5, testcase5.q)
    result5 = soln.lowestCommonAncestor(rootnode5, p5, q5)
    if result5 is None:
        result5 = TreeNode(None)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5.val}, Correct: {result5.val == testcase5.output}")