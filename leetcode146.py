# 146. LRU Cache
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
#
#
#
# Example 1:
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
# Constraints:
#
# 1 <= capacity <= 3000
# 0 <= key <= 104
# 0 <= value <= 105
# At most 2 * 105 calls will be made to get and put.

from typing import List,Optional

# idea: hashmap to store key-node pairs, doubly linked list to maintain ordering
class ListNode:
    def __init__(self, val=0, key=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.items = {}
        self.capacity = capacity
        # create initial list
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        # connect nodes
        self.right.prev = self.left
        self.left.next = self.right

    def get(self, key: int) -> int:
        if key in self.items:
            valnode = self.items[key]
            val = valnode.val
            # update cache ordering
            # remove from old position
            if valnode.prev:
                valnode.prev.next = valnode.next
            if valnode.next:
                valnode.next.prev = valnode.prev

            # add to end of list
            valnode.next = self.right
            valnode.prev = self.right.prev
            self.right.prev = valnode
            valnode.prev.next = valnode
        else:
            val = -1

        return val

    def put(self, key: int, value: int) -> None:
        # update value
        if key in self.items:
            valnode = self.items[key]
            valnode.val = value
        # else add new value
        else:
            valnode = ListNode(value, key)
            self.items[key] = valnode
            # check capacity
            if self.capacity > 0:
                self.capacity -= 1
            else:
                # evict LRU item
                nodetoremove = self.left.next
                self.items.pop(nodetoremove.key, None)
                self.left.next = nodetoremove.next
                nodetoremove.next.prev = self.left

        # remove from old position
        if valnode.prev:
            valnode.prev.next = valnode.next
        if valnode.next:
            valnode.next.prev = valnode.prev

        # add to end of list
        valnode.next = self.right
        valnode.prev = self.right.prev
        self.right.prev = valnode
        valnode.prev.next = valnode


class myLRUCache:

    def __init__(self, capacity: int):
        # create cache hashmap
        self.cache = {}
        self.capacity = capacity

        # create linked list dummy nodes
        self.dummyleft = ListNode(-1)
        self.dummyright = ListNode(-1)
        self.dummyleft.next = self.dummyright
        self.dummyright.prev = self.dummyleft

    def get(self, key: int) -> int:
        # get value if exists and move node to end of list
        # becomes most recently used
        node = self.cache.get(key, ListNode(-1))
        if node.val > -1:
            # key found, update recent used status
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = self.dummyright.prev
            self.dummyright.prev.next = node
            self.dummyright.prev = node
            node.next = self.dummyright

        print("returning node with key:", key, "from cache:", self.cache)
        return node.val

    def put(self, key: int, value: int) -> None:
        # create new node
        newnode = ListNode(value, key)

        # evict LRU node if cache at capacity
        if len(self.cache) >= self.capacity:
            # remove node connections
            lrunode = self.dummyleft.next
            self.dummyleft.next = lrunode.next
            lrunode.next.prev = self.dummyleft
            # delete from cache map
            print(lrunode.key)
            self.cache.pop(lrunode.key)
            print("popped:", self.cache)

        # remove old node if necessary
        oldnode = self.cache.get(key, None)
        if oldnode is not None:
            oldnode.prev.next = oldnode.next
            oldnode.next.prev = oldnode.prev

        # add/update node to hashmap
        self.cache[key] = newnode

        # add new node to end of list
        self.dummyright.prev.next = newnode
        newnode.prev = self.dummyright.prev
        newnode.next = self.dummyright
        self.dummyright.prev = newnode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class testcase1:
    input = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    inputvals = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    output = [None, None, None, 1, None, -1, None, -1, 3, 4]

class testcase3:
    input = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    inputvals = [[2], [1, 0], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    output = [None, None, None, 0, None, -1, None, -1, 3, 4]

class testcase4:
    input = ["LRUCache", "get", "put", "get", "put", "put", "get", "get"]
    inputvals = [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
    output = [None, -1, None, -1, None, None, 2, 6]


