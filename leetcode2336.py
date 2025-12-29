# 2336. Smallest Number in Infinite Set
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
#
# Implement the SmallestInfiniteSet class:
#
# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
#
#
# Example 1:
#
# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]
#
# Explanation
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
# smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
#                                    // is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
#
#
# Constraints:
#
# 1 <= num <= 1000
# At most 1000 calls will be made in total to popSmallest and addBack.

from typing import List, Optional


class SmallestInfiniteSet:

    def __init__(self):
        return

    def popSmallest(self) -> int:
        return

    def addBack(self, num: int) -> None:
        return


import heapq
class mySmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.in_heap = [i for i in range(1, 1001)]
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        removed = heapq.heappop(self.heap)
        self.in_heap[removed - 1] = None
        return removed

    def addBack(self, num: int) -> None:
        # check if num is not in heap, then push
        if self.in_heap[num - 1] is None:
            heapq.heappush(self.heap, num)
            self.in_heap[num - 1] = num

        return None

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

class testcase1:
    input = ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest",
     "popSmallest", "popSmallest"]
    inputvals = [[], [2], [], [], [], [1], [], [], []]
    output = [None, None, 1, 2, 3, None, 1, 4, 5]


if __name__ == '__main__':
    # create object instance
    obj = mySmallestInfiniteSet()

    # test example 1
    # implement custom
    obj.addBack(2)
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
    obj.addBack(1)
    print(obj.popSmallest())
    print(obj.popSmallest())
    print(obj.popSmallest())
