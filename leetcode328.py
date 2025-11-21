# 328. Odd Even Linked List
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
#
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# Example 2:
#
#
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
#
#
# Constraints:
#
# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.val <= 106

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

# https://leetcode.com/problems/odd-even-linked-list/solutions/133345/with-detailed-explanation-python-by-geom-d23r
class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        odd = head  # Both of them point at the first node of the target linked list
        even = head.next  # doesn't matter even there's only one node in the linked list (even will become None)
        eHead = even  # We have to keep where the even-node list starts

        while even and even.next:  # won't get in the loop at first if there's only one node in the linked list
            # both even and even.next are necessary condition because even might point to None, which has no attribute 'next'
            # AND, why these two, small discussion by myself as below
            odd.next = odd.next.next
            even.next = even.next.next
            # After these two ops, odd/even still points at its original place
            # Therefore, we move them to the next node repectively
            odd = odd.next
            even = even.next

        odd.next = eHead  # the odd pointer currently points at the last node of the odd-node list

        return head  # We keep the start of the odd-node list in the first of our code


class mySolution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n), two-pointer, maintain pointers to even/odd nodes
        # reassign .next to point to .next.next
        # end when pointers reach end of list, set odd.next to the head of even linked list

        # handle empty list
        if head is None:
            return head

        odd, even = head, head.next
        dummy = ListNode(-1)
        dummy.next = even  # maintain pointer to start of even
        while odd.next is not None and even is not None:
            # reassign .next
            odd.next = odd.next.next  # even.next
            if even.next is not None:
                even.next = even.next.next

            # move pointers if next pointer exists
            if odd.next is not None:
                odd = odd.next
            if even.next is not None:
                even = even.next

        # connect odd to start of even
        odd.next = dummy.next

        return head


class testcase1:
    head = [1,2,3,4,5]
    output = [1,3,5,2,4]

class testcase2:
    head = [2,1,3,5,6,4,7]
    output = [2,3,6,7,1,5,4]

# ai generated
class testcase3:
    head = [1,2,3,4,5,6]
    output = [1,3,5,2,4,6]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    linkedhead1 = build_linked_list(testcase1.head)
    result1 = soln.oddEvenList(linkedhead1)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    linkedhead2 = build_linked_list(testcase2.head)
    result2 = soln.oddEvenList(linkedhead2)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")

    # test example 3
    linkedhead3 = build_linked_list(testcase3.head)
    result3 = soln.oddEvenList(linkedhead3)
    listresult3 = linked_list_to_list(result3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {listresult3}, Correct: {listresult3 == testcase3.output}")