# 141. Linked List Cycle
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
# Constraints:
#
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
#
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None





class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        return False


def build_linked_list(head: List) -> ListNode:
    if not head:
        return None

    node = ListNode(0)
    start = node
    for n in head:
        nextnode = ListNode(n)
        node.next = nextnode
        node = nextnode

    return start.next


class mySolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use slow, fast pointers
        # if fast pointer == slow before slow reaches end of list, then True, else False
        slow, fast = head, head


        return False

class testcase1:
    head = [3,2,0,-4]
    pos = 1
    output = True

class testcase2:
    head = [1,2]
    pos = 0
    output = True
    # headNode = buildLinkedList(head)

class testcase3:
    head = [1]
    pos = -1
    output = False
    # headNode = buildLinkedList(head)


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    headNode = build_linked_list(testcase1.head)
    result1 = soln.hasCycle(headNode)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    headNode = build_linked_list(testcase2.head)
    result2 = soln.hasCycle(headNode)
    print(f"Example 1 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")
