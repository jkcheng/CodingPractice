# 92. Reverse Linked List II
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
# Constraints:
#
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
# Follow up: Could you do it in one pass?

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(head: List[int]) -> ListNode:
    if len(head) == 0:
        return None

    dummy = ListNode(0)
    cur = dummy
    for n in head:
        node = ListNode(n)
        cur.next = node
        cur = node

    return dummy.next

def linked_list_to_list(head: ListNode) -> List[int]:
    output = []
    if head is None:
        return output

    while head:
        output.append(head.val)
        head = head.next

    return output

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        # Comparing with Problem 206: just need to find the start position
        # then reverse (same as 206)

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = dummy.next

        # find the position
        for i in range(1, m):
            cur = cur.next
            pre = pre.next

        # reverse
        for i in range(n - m):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp

        return dummy.next

class mySolution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # traverse list, reverse pointers only when node count is between left and right inclusive
        before, after = None, None
        nodecount = 1

        dummy = ListNode(0)
        dummy.next = head
        node = head
        while node is not None:  # [1,2]
            after = node.next  # None
            # move pointers only if in range
            if nodecount >= left and nodecount <= right:
                # save node before reversal
                if nodecount == left:
                    beforereverse = before  # None
                    startreverse = node  # 1
                if nodecount == right:
                    afterreverse = node.next  # None
                    endreverse = node  # 2

                node.next = before

            before = node  # 2
            node = after  # None
            nodecount += 1

        # fix pointers
        startreverse.next = afterreverse  # None
        if beforereverse is not None:
            beforereverse.next = endreverse  # 2

        return head if beforereverse else endreverse

class testcase1:
    head = [1, 2, 3, 4, 5]
    left = 2
    right = 4
    output = [1, 4, 3, 2, 5]
    linkedlist = build_linked_list(head)

class testcase2:
    head = [5]
    left = 1
    right = 1
    output = [5]
    linkedlist = build_linked_list(head)

class testcase3:
    head = [3, 5]
    left = 1
    right = 2
    output = [5, 3]
    linkedlist = build_linked_list(head)

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.reverseBetween(testcase1.linkedlist, testcase1.left, testcase1.right)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    result2 = soln.reverseBetween(testcase2.linkedlist, testcase2.left, testcase2.right)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")

    # test example 3
    result3 = soln.reverseBetween(testcase3.linkedlist, testcase3.left, testcase3.right)
    listresult3 = linked_list_to_list(result3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {listresult3}, Correct: {listresult3 == testcase3.output}")