# 133. Clone Graph
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
#
#
# Test case format:
#
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
#
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
#
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
#
#
#
# Example 1:
#
#
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# Example 2:
#
#
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
# Example 3:
#
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
#
#
# Constraints:
#
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

from typing import List,Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# todo
# create graph from adjList

# create adjList from graph


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited_nodes = {}

        # loop_condition?
        def dfs(node):
            if not node:
                return None

            if node not in visited_nodes:
                newnode = Node(node.val)
                visited_nodes[node] = newnode
                newnode.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
            else:
                newnode = visited_nodes[node]

            return newnode

        newgraph = dfs(node)

        return newgraph


class mySolution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # step through original graph and create copies of nodes
        # create mapping of node -> copy_node
        # step through original graph and use mapping to link node copies into new graph

        mapping = {}
        # copy original nodes, add to mapping
        start = node
        queue = []  # use deque for optimization

        if start is not None:
            queue.append(start)
        while len(queue) > 0:
            node = queue.pop(0)

            # copy node
            new_node = Node(node.val)

            # add to mapping
            mapping[node] = new_node

            # add neighbors to queue if not already copied
            for neighbor in node.neighbors:
                if neighbor not in mapping.keys():
                    queue.append(neighbor)

        # set neighbors in copied nodes
        queue = []
        if start is not None:
            queue.append(start)

        new_start = mapping.get(start, None)

        seen = set()
        while len(queue) > 0:
            node = queue.pop(0)
            seen.add(node)

            # set neighbors
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_node.neighbors.append(mapping[neighbor])
                if neighbor not in seen and neighbor not in queue:
                    queue.append(neighbor)

        return new_start  # if start is not None else None


class testcase1:
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    output = [[2,4],[1,3],[2,4],[1,3]]

class testcase2:
    adjList = [[]]
    output = [[]]

class testcase3:
    adjList = []
    output = []

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.cloneGraph(testcase1.adjList)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.cloneGraph(testcase2.adjList)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.cloneGraph(testcase3.adjList)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )