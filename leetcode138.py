# 138. Copy List with Random Pointer
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
#
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.
#
# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
#
# Return the head of the copied linked list.
#
# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.
#
#
#
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# Example 3:
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
#
# Constraints:
#
# 0 <= n <= 1000
# -104 <= Node.val <= 104
# Node.random is null or is pointing to some node in the linked list.

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def build_linked_list(head: List[List[int]]) -> Node:
    if not head: # or len(head) == 0:
        return None

    dummy = Node(0)
    cur = dummy
    mapping = {None:None} # mapping for storing new nodes as idx:node
    idx = 0
    for nextval,randomidx in head:
        newnode = Node(nextval)
        mapping[idx] = newnode
        cur.next = newnode
        cur = cur.next
        idx += 1

    # iterate again to assign random pointer
    cur = dummy.next
    for nextval,randomidx in head:
        cur.random = mapping[randomidx]
        cur = cur.next

    return dummy.next

def linked_list_to_list(head: Node) -> List[List[int]]:
    output = []

    # need to parse twice just like building the linked list
    cur = head
    mapping = {None:None}
    while cur is not None:
        output.append([cur.val,None])
        idx = len(output)-1
        mapping[cur] = idx # use actual node as key in case of duplicate node.val
        cur = cur.next

    cur = head
    idx = 0
    while cur is not None:
        # randomval = cur.random.val if cur.random else None
        randomidx = mapping[cur.random]
        output[idx][1] = randomidx
        cur = cur.next
        idx += 1

    return output


class Solution:
    # two pass idea: build normal linked list nodes and insert into hashmap linking old node -> new, then traverse oldlist and update random pointer to nodes using array indexes
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create new nodes and add to hashmap
        oldnode = head
        nodes = {None: None}
        # prevnewnode = None
        while oldnode:
            newnode = Node(oldnode.val)
            nodes[oldnode] = newnode
            oldnode = oldnode.next

        # assign pointers for new list
        oldnode = head
        while oldnode:
            newnode = nodes[oldnode]
            newnode.next = nodes[oldnode.next]
            newnode.random = nodes[oldnode.random]

            oldnode = oldnode.next

        return nodes[head]

class mySolution(object):
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # two-pass: create hash table to serve as a lookup table
        # key = old_node, value = new_node

        # create hash table map
        mapping = {}  # alternatively initialize to {None:None} to avoid needing to use .get() with default None
        oldhead = head
        cur = head
        while cur is not None:
            new_node = Node(cur.val)
            mapping[cur] = new_node
            cur = cur.next

        # create new linked list
        newhead = mapping.get(oldhead, None)
        cur = newhead
        oldcur = oldhead
        while cur is not None:
            cur.next = mapping.get(oldcur.next, None)
            cur.random = mapping.get(oldcur.random, None)
            cur = cur.next
            oldcur = oldcur.next

        return newhead


class testcase1:
    head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    linkedlisthead = build_linked_list(head)
    output = [[7,None],[13,0],[11,4],[10,2],[1,0]]

class testcase2:
    head = [[1,1],[2,1]]
    linkedlisthead = build_linked_list(head)
    output = [[1,1],[2,1]]

class testcase3:
    head = [[3, None], [3, 0], [3, None]]
    linkedlisthead = build_linked_list(head)
    output =  [[3, None], [3, 0], [3, None]]

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.copyRandomList(testcase1.linkedlisthead)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    result2 = soln.copyRandomList(testcase2.linkedlisthead)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")

    # test example 3
    result3 = soln.copyRandomList(testcase3.linkedlisthead)
    listresult3 = linked_list_to_list(result3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {listresult3}, Correct: {listresult3 == testcase3.output}")