# 210. Course Schedule II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
#
#
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:
#
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:
#
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#
#
# Constraints:
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.

from typing import List,Optional


# DFS solution using states array
class Solution:
    def buildAdjList(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        return adj_list

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = self.buildAdjList(numCourses, prerequisites)
        # completed = set() # courses already completed
        course_order = []

        def dfs(course):
            # course explored and no cycle found
            if states[course] == 1:
                return False

            # course being explored, so cycle found
            if states[course] == -1:
                return True

            states[course] = -1
            prereqs = adj_list[course]
            for prereq in prereqs:
                if dfs(prereq):
                    return True

            # now that prereqs are satisfied, can take course
            course_order.append(course)

            # set course to explored
            states[course] = 1
            return False

        # states array to track courses status
        # 0 = initial state, not explored yet
        # 1 = fully explored and found to have no loops in it's prereqs
        # -1 = currently being explored; if encounted while exploring then there is a loop and courses cannot be finished
        states = [0 for _ in range(numCourses)]

        for course in range(numCourses):
            if dfs(course):  # if cycle found, return empty array
                return []

        return course_order


class mySolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS: model courses and prereqs as graph and try to detect cycle of prereqs
        # start at final course in series and record prereq sequence

        # build graph of prereqs
        prereqs = {}
        for course, prereq in prerequisites:
            prereqs[course] = prereqs.get(course, []) + [prereq]

        # explore graph
        # use course_state to check state of a course
        # 0 = not explored yet
        # 1 = explored and completed with no cycles
        # -1 = currently exploring OR explored with cycle found
        course_state = [0] * numCourses

        def detect_cycle(course):
            # course already explored with no cycles
            if course_state[course] == 1:
                return False

            # course currently being explored in DFS stack
            if course_state[course] == -1:
                return True

            # visit course and check prereqs
            course_state[course] = -1
            course_prereqs = prereqs.get(course, [])
            for prereq in course_prereqs:
                if detect_cycle(prereq):
                    return True

            # no cycle found, add course to list and remove from visited
            courselist.append(course)
            course_state[course] = 1

        # explore courses in order
        courselist = []
        for course in range(numCourses):
            if detect_cycle(course):
                return []

        return courselist


class testcase1:
    numCourses = 2
    prerequisites = [[1, 0]]
    output = [0, 1]

class testcase2:
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    output = [0, 2, 1, 3]

class testcase3:
    numCourses = 1
    prerequisites = []
    output = [0]

class testcase4:
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    output = []

if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.findOrder(testcase1.numCourses, testcase1.prerequisites)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.findOrder(testcase2.numCourses, testcase2.prerequisites)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")

    # test example 3
    result3 = soln.findOrder(testcase3.numCourses, testcase3.prerequisites)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {testcase3.output == result3}")

    # test example 4
    result4 = soln.findOrder(testcase4.numCourses, testcase4.prerequisites)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {testcase4.output == result4}")
