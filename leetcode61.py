# 61. Rotate List
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, rotate the list to the right by k places.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

from typing import List,Optional


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
    while cur is not None:
        nodes.append(cur.val)
        cur = cur.next

    return nodes

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        return


class mySolution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # O(2n): traverse list to end and link last node to first, creating cycle
        # traverse to correct end node of final rotated config and break link
        # return old next node as head

        # link end node to head, create cycle
        # dummy = ListNode(-1)
        # dummy.next = head
        cur = head
        nodecount = 1 if cur is not None else 0
        while cur is not None and cur.next is not None:
            cur = cur.next
            nodecount += 1

        if cur is not None:
            cur.next = head

        # find correct final node in rotated config
        if nodecount > 0:
            steps = nodecount - (k % nodecount) - 1  # ?
        else:
            steps = 0
        cur = head
        while cur is not None and steps > 0:
            cur = cur.next
            steps -= 1

        if cur is not None:
            newhead = cur.next
            cur.next = None
        else:
            newhead = None
        return newhead

class testcase1:
    head = [1, 2, 3, 4, 5]
    k = 2
    output = [4, 5, 1, 2, 3]
    linkedlisthead = build_linked_list(head)

class testcase2:
    head = [0, 1, 2]
    k = 4
    output = [2, 0, 1]
    linkedlisthead = build_linked_list(head)

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.rotateRight(testcase1.linkedlisthead, testcase1.k)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    result2 = soln.rotateRight(testcase2.linkedlisthead, testcase2.k)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")