# 21. Merge Two Sorted Lists
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(head: List[int]) -> ListNode:
    if not head: # or if len(head) == 0
        return None

    dummy = ListNode(0)
    cur = dummy
    for n in head:
        node = ListNode(n)
        cur.nest = node
        cur = node

    return dummy.next

def linked_list_to_list(head: ListNode) -> List[int]:
    res = []
    if not head: # or if head is None
        return res

    while head: # or if head is not None
        res.append(head.val)
        head = head.next

    return res

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cur = head

        while cur and (list1 or list2):
            if (list2 == None) or ((list1 and list2) and (list1.val <= list2.val)):
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        return head.next

class mySolution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers, copy smaller value to new list and move pointer forward
        dummy = ListNode(0)
        cur = dummy

        # build new list by copying smaller value
        while list1 or list2:
            l1 = list1.val if list1 else None
            l2 = list2.val if list2 else None

            if (l1 is not None) and (l2 is not None) and l1 < l2:
                node = ListNode(l1)
                list1 = list1.next
            elif l2 is not None:  # l1 >= l2
                node = ListNode(l2)
                list2 = list2.next
            elif l1 is not None:
                node = ListNode(l1)
                list1 = list1.next

            cur.next = node
            cur = node

        return dummy.next

class testcase1:
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    output = [1,1,2,3,4,4]
    linkedlist1 = build_linked_list(list1)
    linkedlist2 = build_linked_list(list2)

class testcase2:
    list1 = []
    list2 = []
    output = []
    linkedlist1 = build_linked_list(list1)
    linkedlist2 = build_linked_list(list2)

class testcase3:
    list1 = []
    list2 = [0]
    output = [0]
    linkedlist1 = build_linked_list(list1)
    linkedlist2 = build_linked_list(list2)

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    linkedlistresult1 = soln.mergeTwoLists(testcase1.linkedlist1, testcase1.linkedlist2)
    result1 = linked_list_to_list(linkedlistresult1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    linkedlistresult2 = soln.mergeTwoLists(testcase2.linkedlist1, testcase2.linkedlist2)
    result2 = linked_list_to_list(linkedlistresult2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    linkedlistresult3 = soln.mergeTwoLists(testcase3.linkedlist1, testcase3.linkedlist2)
    result3 = linked_list_to_list(linkedlistresult3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")
