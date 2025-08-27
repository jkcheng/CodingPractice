# 148. Sort List
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, return the list after sorting it in ascending order.
#
#
#
# Example 1:
#
#
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:
#
#
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:
#
# Input: head = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
#
#
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

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
    ans = []
    while head is not None:
        ans.append(head.val)
        head = head.next

    return ans

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        return

class mySolution:
    # classic merge sort: split list into two halves recursively, merge two sorted halves
    # use fast/slow pointers to find half node in linked list
    # break list into two halves when finding midpoint
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case: if list is empty or only has one value
        if head is None or head.next is None:
            return head

        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeList(left, right)

    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        # use fast.next and fast.next.next existing as stopping criteria
        # slow will stop at left half for even n and exact mid for odd n
        # slow represents last item of first half, set slow.next = None to sever list
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # get first node of second half
        mid = slow.next
        # sever list into two halves
        slow.next = None
        return mid  # returns first node of second half

    def mergeList(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        # dummy.next = head1

        cur = dummy
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
                # cur = cur.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head1 is not None:
            cur.next = head1
        else:
            cur.next = head2

        return dummy.next


class testcase1:
    head = [4,2,1,3]
    output = [1,2,3,4]

class testcase2:
    head = [-1,5,3,4,0]
    output = [-1,0,3,4,5]

class testcase3:
    head = []
    output = []

# ai generated
class testcase4:
    head = [1,2,3,4,5,6,7,8,9,10]
    output = [1,2,3,4,5,6,7,8,9,10]

class testcase5:
    head = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    output = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    head_node = build_linked_list(testcase1.head)
    result_node1 = soln.sortList(head_node)
    result1 = linked_list_to_list(result_node1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    head_node = build_linked_list(testcase2.head)
    result_node2 = soln.sortList(head_node)
    result2 = linked_list_to_list(result_node2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    head_node = build_linked_list(testcase3.head)
    result_node3 = soln.sortList(head_node)
    result3 = linked_list_to_list(result_node3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    head_node = build_linked_list(testcase4.head)
    result_node4 = soln.sortList(head_node)
    result4 = linked_list_to_list(result_node4)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {result4}, Correct: {result4 == testcase4.output}")

    # test example 5
    head_node = build_linked_list(testcase5.head)
    result_node5 = soln.sortList(head_node)
    result5 = linked_list_to_list(result_node5)
    print(f"Example 5 - Expected: {testcase5.output}, Got: {result5}, Correct: {result5 == testcase5.output}")