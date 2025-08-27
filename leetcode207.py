# 207. Course Schedule
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
#
# Constraints:
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.


from typing import List, Optional

# cycle detection using DFS
class Solution:
    # def buildAdjList(self, numCourses: int, prerequisites: List[List[int]]) -> List:
    #     adj_list = {i:[] for i in range(numCourses)}
    #     for dest, source in prerequisites:
    #         adj_list[dest].append(source)
    #     return adj_list

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for dest, source in prerequisites:
            adj_list[dest].append(source)

        def detectCycle(course):
            if course in visited:
                return True

            prereqs = adj_list[course]
            if len(prereqs) == 0:  # no rerequisites
                return False

            visited.add(course)
            for prereq in prereqs:
                if detectCycle(prereq):
                    return True

            visited.remove(course)
            # optimization: remove prereqs on course since it is confirmed to NOT have cycle
            adj_list[course] = []
            return False

        for course in adj_list.keys():
            visited = set()
            if detectCycle(course):
                return False

        return True


class mySolution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # assumption: course NOT in prerequisites = they have no prereqs and are not prereqs of anything else
        # graph traversal with cycle detection: model prereqs as graph and detect if cycle exists

        # build graph
        graph = {}
        for course, prereq in prerequisites:
            # prereqs = graph.get(a,[])
            # prereqs.append(b)
            # graph[a] = prereqs
            graph[course] = graph.get(course, []) + [prereq]

        # BFS: traverse graph starting from 0
        # visited = set()
        # for start in range(numCourses):
        #     # explore graph if start not visited yet
        #     if start not in visited:
        #         queue = [start] # can use deque
        #         while len(queue) > 0:
        #             num_courses = len(queue)
        #             for _ in range(num_courses)
        #                 course = queue.pop(0)
        #                 visited.add(course)
        #                 queue = queue + graph[course] # add all next courses to queue

        # DFS: detect cycle
        visited = set()

        def detect_cycle(course):
            if course in visited:
                return True

            prereqs = graph.get(course, None)
            if prereqs is None:  # course has no prereqs
                return False

            # check for cycle
            visited.add(course)
            for prereq in prereqs:
                if prereq in visited:
                    return True
                elif detect_cycle(prereq):
                    return True

            # done checking course, remove from visited
            visited.remove(course)

            return False

        # check each course that has prereqs
        for course in graph.keys():
            visited = set()
            if detect_cycle(course):
                return False  # all courses cannot be completed

        return True


class testcase1:
    numCourses = 2
    prerequisites = [[1,0]]
    output = True

class testcase2:
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    output = False


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.canFinish(testcase1.numCourses, testcase1.prerequisites)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}" )

    # test example 2
    result2 = soln.canFinish(testcase2.numCourses, testcase2.prerequisites)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}" )