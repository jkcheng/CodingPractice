# 380. Insert Delete GetRandom O(1)
# Solved
# Medium
# Topics
# Companies
# Implement the RandomizedSet class:
#
# RandomizedSet() Initializes the RandomizedSet object.
#
# bool insert(int val) Inserts an item val into the set if not present
# Returns true if the item was not present, false otherwise.
#
# bool remove(int val) Removes an item val from the set if present.
# Returns true if the item was present, false otherwise.
#
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one
# element exists when this method is called). Each element must have the same probability of being returned.
#
# You must implement the functions of the class such that each function works in average O(1) time complexity.
#
#
#
# Example 1:
#
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
#
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
#
#
# Constraints:
#
# -231 <= val <= 231 - 1
# At most 2 * 105 calls will be made to insert, remove, and getRandom.
# There will be at least one element in the data structure when getRandom is called.

# https://leetcode.com/problems/insert-delete-getrandom-o1/solutions/85397/simple-solution-in-python
# We just keep track of the index of the added elements, so when we remove them, we copy the last one into it.
# https://stackoverflow.com/questions/15993447/python-data-structure-for-efficient-add-remove-and-random-choice

from typing import List
import random

class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.validxs = {}

    def insert(self, val: int) -> bool:
        if val not in self.validxs:
            self.vals.append(val)
            self.validxs[val] = len(self.vals)-1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.validxs:
            # get index of val and lastval in nums to swap positions before removal
            validx = self.validxs[val]
            lastval = self.vals[-1]

            # swap positions, idx for easy removal
            self.vals[validx], self.vals[-1] = lastval, val
            self.validxs[lastval] = validx

            # remove last value and idx
            self.vals.pop()
            self.validxs.pop(val)
            return True

        return False

    def getRandom(self) -> int:
        randidx = random.random()*len(self.vals)

        return self.vals[int(randidx)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class testcase1:
    method_sequence = ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
    input = [[], [0], [1], [0], [2], [1], []]

class testcase2:
    method_sequence = ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
    input = [[],[0],[1],[0],[2],[1],[]]

class testcase3:
    citations = [3, 0, 6, 1, 5, 4]

class testcase4:
    citations = [1]

class testcase5:
    citations = [9,9,9]