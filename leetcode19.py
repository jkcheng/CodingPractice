# 19. Remove Nth Node From End of List
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(head: List[int]) -> Optional[ListNode]:
    if len(head) == 0:
        return None

    dummy = ListNode(-1)
    cur = dummy
    for n in head:
        node = ListNode(n)
        cur.next = node
        cur = node

    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    nodes = []
    if head is None:
        return nodes

    cur = head
    while cur:
        nodes.append(cur.val)
        cur = cur.next

    return nodes

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # remove node
        dummy = ListNode(-1)
        dummy.next = head
        left = head

        # move right pointer n places
        right = head
        while right and n > 0:
            right = right.next
            n -= 1

        # remove node
        left = dummy
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

class mySolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two-pass: count how long list is, then move len(linkedlist)-n steps and remove that node
        nodecount = 0
        cur = head
        while cur is not None:
            nodecount += 1
            cur = cur.next

        steps = nodecount - n
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head
        while cur is not None and steps > 0:
            steps -= 1
            prev = cur
            cur = cur.next

        # remove cur node
        prev.next = cur.next

        return dummy.next

class mySolution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # one-pass: maintain two pointers that are n distance apart
        # remove node at second pointer when lead pointer falls off list
        dummy = ListNode(-1)
        dummy.next = head
        lead = head
        cur = head
        prev = dummy
        while lead is not None:
            lead = lead.next
            if n > 0:
                n -= 1
            else:
                prev = prev.next
                cur = cur.next

        # remove node at cur
        prev.next = cur.next

        return dummy.next

class testcase1:
    head = [1, 2, 3, 4, 5]
    n = 2
    output = [1, 2, 3, 5]
    linkedhead = build_linked_list(head)

class testcase2:
    head = [1]
    n = 1
    output = []
    linkedhead = build_linked_list(head)

class testcase3:
    head = [1, 2]
    n = 1
    output = [1]
    linkedhead = build_linked_list(head)

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution2()

    # test example 1
    result1 = soln.removeNthFromEnd(testcase1.linkedhead, testcase1.n)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    result2 = soln.removeNthFromEnd(testcase2.linkedhead, testcase2.n)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")