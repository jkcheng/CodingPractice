# 399. Evaluate Division
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
#
# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
#
#
#
# Example 1:
#
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation:
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
# Example 2:
#
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:
#
# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
#
#
# Constraints:
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.

from typing import List, Optional

# https://leetcode.com/problems/evaluate-division/solutions/88275/python-fast-bfs-solution-with-detailed-e-ocvb
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        return


from collections import defaultdict
class mySolution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # DFS, model variables as nodes with values being edge values between them
        # a/b = 2.0 becomes a -- 2.0 --> b)
        # All division operations can be seen as traversing this graph along appropriate nodes and edges
        # to reach from source to destination, with numerator as source and denomination as destination.
        # When traversing reverse direction invert the value of the edge.
        # e.g.: a/b = 2, c/d = 3 becomes a -- 2.0 --> b -- 3.0 --> c.
        # a/c = 2*3, c/a = (c/b)^-1 * (b/a)^-1 = 1/3 * 1/2

        # use nested dictionary to represent graph
        # graph[a][b] represents traversing a -> b
        graph = defaultdict(dict)  # makes setting up nested dict easier
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            v = values[i]

            # graph[a] = graph.get(a,{})[b]
            graph[a][b] = v
            graph[b][a] = 1 / v

        # iterate through queries and find path from a -> b in graph
        # if a or be not in graph, then return -1
        ans = []
        for q in queries:
            a = q[0]
            b = q[1]
            # if either not in graph
            if a not in graph or b not in graph:
                ans.append(-1)
                continue

            # bfs search through graph
            queue = [(a, 1.0)]
            visited = set()
            found = False
            while len(queue) > 0:
                node, dist = queue.pop(0)
                if node == b:  # if node in queue is our destination, add answer
                    ans.append(dist)
                    found = True
                    break
                visited.add(node)
                for dest in graph[node]:
                    if dest not in visited:
                        new_dist = dist * graph[node][dest]
                        queue.append((dest, new_dist))

            # if queue finished without finding node b
            if not found:
                ans.append(-1)

        return ans

class mySolution2:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # O(n), n = len(equations + queries), model operations as a graph
        # e.g. a / b = 2 becomes a -> b with edge value 2
        # a / b is forward direction, b/a is reverse
        # any a/x can be modeled as multiplying edge values in the path a -> b -> x

        # # dfs search through graph
        # def dfs(graph, a, b, ans) -> float:
        #     if a not in graph:
        #         return 1

        #     for dest_node,val in graph[a].items():
        #         if dest_node == b:
        #             return ans * val

        #         # continue searching through dest_node to find b
        #         ans *= dfs(graph, dest_node, b, ans)

        # create adjacency list as nested dict
        # graph[a] = {b: val}
        graph = {}
        for (a, b), val in zip(equations, values):
            # set division result as graph[a][b]
            dests = graph.get(a, {})
            dests[b] = val
            graph[a] = dests

            # set reverse direction for easier lookup
            rdests = graph.get(b, {})
            rdests[a] = 1 / val
            graph[b] = rdests

        # evaluate queries
        ans = []
        for q1, q2 in queries:
            a = q1
            b = q2
            # if either not in graph
            if a not in graph or b not in graph:
                ans.append(-1)
                continue

            # bfs search through graph
            queue = [(a, 1.0)]
            visited = set()
            found = False
            while len(queue) > 0:
                node, dist = queue.pop(0)
                if node == b:  # if node in queue is our destination, add answer
                    ans.append(dist)
                    found = True
                    break
                visited.add(node)
                for dest in graph[node]:
                    if dest not in visited:
                        new_dist = dist * graph[node][dest]
                        queue.append((dest, new_dist))

            # if queue finished without finding node b
            if not found:
                ans.append(-1)

        return ans


class testcase1:
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    output = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

class testcase2:
    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    output = [3.75000, 0.40000, 5.00000, 0.20000]

class testcase3:
    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    output = [0.50000, 2.00000, -1.00000, -1.00000]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.calcEquation(testcase1.equations, testcase1.values, testcase1.queries)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.calcEquation(testcase2.equations, testcase2.values, testcase2.queries)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )

    # test example 3
    result3 = soln.calcEquation(testcase3.equations, testcase3.values, testcase3.queries)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}" )