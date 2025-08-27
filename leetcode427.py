# 427. Construct Quad Tree
# Medium
# Topics
# premium lock icon
# Companies
# Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.
#
# Return the root of the Quad-Tree representing grid.
#
# A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:
#
# val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
# isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
# class Node {
#     public boolean val;
#     public boolean isLeaf;
#     public Node topLeft;
#     public Node topRight;
#     public Node bottomLeft;
#     public Node bottomRight;
# }
# We can construct a Quad-Tree from a two-dimensional area using the following steps:
#
# If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
# If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
# Recurse for each of the children with the proper sub-grid.
#
# If you want to know more about the Quad-Tree, you can refer to the wiki.
#
# Quad-Tree format:
#
# You don't need to read this section for solving the problem. This is only if you want to understand the output format here. The output represents the serialized format of a Quad-Tree using level order traversal, where null signifies a path terminator where no node exists below.
#
# It is very similar to the serialization of the binary tree. The only difference is that the node is represented as a list [isLeaf, val].
#
# If the value of isLeaf or val is True we represent it as 1 in the list [isLeaf, val] and if the value of isLeaf or val is False we represent it as 0.
#
#
#
# Example 1:
#
#
# Input: grid = [[0,1],[1,0]]
# Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
# Explanation: The explanation of this example is shown below:
# Notice that 0 represents False and 1 represents True in the photo representing the Quad-Tree.
#
# Example 2:
#
#
#
# Input: grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
# Output: [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# Explanation: All values in the grid are not the same. We divide the grid into four sub-grids.
# The topLeft, bottomLeft and bottomRight each has the same value.
# The topRight have different values so we divide it into 4 sub-grids where each has the same value.
# Explanation is shown in the photo below:
#
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# n == 2x where 0 <= x <= 6

from typing import List, Optional

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

# TODO: reverse function to output list format of QuadTree
def quad_tree_to_list(root: Node) -> List[List[int]]:

    return


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        return


class mySolution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # recursive, divide and conquer
        # split grid into quadrants
        # if values in qudrants are the same, isLeaf = True
        # if not, recurse and perform quadrant splitting and value checking

        def recurse(grid: List[List[int]]) -> Node:
            # create default leaf node
            root = Node(grid[0][0], True, None, None, None, None)

            # check if current grid has same values
            if is_same(grid):
                return root
            else:  # recurse
                mid = len(grid) // 2
                root.isLeaf = False
                # slicing into quadrants requires list comprehension
                root.topLeft = recurse([row[0:mid] for row in grid[0:mid]])
                root.topRight = recurse([row[mid:] for row in grid[0:mid]])
                root.bottomLeft = recurse([row[0:mid] for row in grid[mid:]])
                root.bottomRight = recurse([row[mid:] for row in grid[mid:]])

            return root

        def is_same(grid):
            n = len(grid)
            val = grid[0][0]
            for i in range(n):
                for j in range(n):
                    if grid[i][j] != val:
                        return False

            return True

        return recurse(grid)

class mySolution2:
    # alternative solution: use recursion to determine if grid values are same
    def construct(self, grid: List[List[int]]) -> 'Node':
        # recursive, divide and conquer
        # split grid into quadrants
        # if values in qudrants are the same, isLeaf = True
        # if not, recurse and perform quadrant splitting and value checking

        def recurse(grid: List[List[int]]) -> Node:
            # create default leaf node
            root = Node(grid[0][0], True, None, None, None, None)

            # return default leaf node if size grid == 1
            if len(grid) == 1:
                return root

            # optimization?: rely on recursion to determine if grid values are same
            # avoid iterating through grid multiple times
            mid = len(grid) // 2
            root.isLeaf = False
            # slicing into quadrants requires list comprehension
            root.topLeft = recurse([row[0:mid] for row in grid[0:mid]])
            root.topRight = recurse([row[mid:] for row in grid[0:mid]])
            root.bottomLeft = recurse([row[0:mid] for row in grid[mid:]])
            root.bottomRight = recurse([row[mid:] for row in grid[mid:]])

            # set current node as leaf if children all have same value
            # and children are all leaves
            if (root.topLeft.val == root.topRight.val == root.bottomLeft.val == root.bottomRight.val) and (
                    root.topLeft.isLeaf and root.topRight.isLeaf and root.bottomLeft.isLeaf and root.bottomRight.isLeaf):
                return Node(root.topRight.val, True, None, None, None, None)

            return root

        return recurse(grid)


class testcase1:
    grid = [[0,1],[1,0]]
    output = [[0,1],[1,0],[1,1],[1,1],[1,0]]

class testcase2:
    grid = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]
    output = [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]

class testcase3:
    grid = [[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1]]
    output = [[0,1],[0,1],[0,1],[0,1],[0,1],[1,1],[1,0],[1,0],[1,0],[1,0],[1,1],[1,0],[1,1],[1,0],[1,0],[1,1],[1,0],[1,0],[1,1],[1,0],[1,1]]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    root1 = soln.construct(testcase1.grid)
    quadtreelist1 = quad_tree_to_list(root1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {quadtreelist1}, Correct: {testcase1.output == quadtreelist1}" )

    # test example 2
    root2 = soln.construct(testcase2.grid)
    quadtreelist2 = quad_tree_to_list(root2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {quadtreelist2}, Correct: {testcase2.output == quadtreelist2}")

    # test example 3
    root3 = soln.construct(testcase3.grid)
    quadtreelist3 = quad_tree_to_list(root3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {quadtreelist3}, Correct: {testcase3.output == quadtreelist3}")
