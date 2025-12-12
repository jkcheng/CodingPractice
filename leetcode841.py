# 841. Keys and Rooms
# Medium
# Topics
# premium lock icon
# Companies
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
#
# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
#
# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
#
#
#
# Example 1:
#
# Input: rooms = [[1],[2],[3],[]]
# Output: true
# Explanation:
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.
# Example 2:
#
# Input: rooms = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
#
#
# Constraints:
#
# n == rooms.length
# 2 <= n <= 1000
# 0 <= rooms[i].length <= 1000
# 1 <= sum(rooms[i].length) <= 3000
# 0 <= rooms[i][j] < n
# All the values of rooms[i] are unique.

from typing import List, Optional


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])

        def dfs(room):
            for neib in rooms[room]:
                if neib not in visited:
                    visited.add(neib)
                    dfs(neib)

        dfs(0)
        return len(visited) == len(rooms)


from collections import deque
class mySolution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # O(n), array, graph traversal, start at index 0 and traverse through all indexes visitable based seen values
        # check if seen indexes matches length of rooms

        visited = set([0])
        queue = deque(rooms[0])

        # traverse rooms
        while len(queue) > 0:
            key = queue.popleft()
            if key not in visited:
                queue.extend(rooms[key])  # add list items in rooms[key] to queue
                # mark room as visited
                visited.add(key)

        return len(visited) == len(rooms)

class mySolution_optimized:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # O(n), array, graph traversal, start at index 0 and traverse through all indexes visitable based seen values
        # check if seen indexes matches length of rooms

        visited = set([0])
        queue = [0]

        # traverse rooms
        while len(queue) > 0:
            key = queue.pop()
            # optimization: only add unvisited rooms to queue
            for k in rooms[key]:
                if k not in visited:
                    queue.append(k)
                    # unintuitive: add new k in queue to visited
                    visited.add(k)
                    # optimization: return early if all rooms visited (including rooms in queue)
                    if len(rooms) == len(visited):
                        return True

        return len(visited) == len(rooms)

class testcase1:
    rooms = [[1], [2], [3], []]
    output = True

class testcase2:
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    output = False


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution_optimized()

    # test example 1
    result1 = soln.canVisitAllRooms(testcase1.rooms)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.canVisitAllRooms(testcase2.rooms)
    print(f"Example 1 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")