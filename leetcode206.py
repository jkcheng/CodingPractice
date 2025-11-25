# 206. Reverse Linked List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
#
# Input: head = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#
#
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(head: List[int]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    cur = dummy
    for n in head:
        node = ListNode(n)
        cur.next = node
        cur = node

    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    nodes = []
    while head is not None:
        nodes.append(head.val)
        head = head.next

    return nodes

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

class mySolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n), two-pointer, connect node to prev node
        prev = None

        while head is not None:
            # maintain pointer to next node
            nextnode = head.next

            # reassign head.next
            head.next = prev

            # move pointers
            prev = head
            head = nextnode

        return prev




class testcase1:
    head = [1,2,3,4,5]
    output = [5,4,3,2,1]

class testcase2:
    head = [1,2]
    output = [2,1]

class testcase3:
    head = []
    output = []

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    linkedhead1 = build_linked_list(testcase1.head)
    result1 = soln.reverseList(linkedhead1)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    linkedhead2 = build_linked_list(testcase2.head)
    result2 = soln.reverseList(linkedhead2)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")

    # test example 3
    linkedhead3 = build_linked_list(testcase3.head)
    result3 = soln.reverseList(linkedhead3)
    listresult3 = linked_list_to_list(result3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {listresult3}, Correct: {listresult3 == testcase3.output}")

