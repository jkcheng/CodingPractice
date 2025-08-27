# 82. Remove Duplicates from Sorted List II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:
#
#
# Input: head = [1,1,1,2,3]
# Output: [2,3]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

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
    if not head:
        return nodes

    cur = head
    while cur is not None:
        nodes.append(cur.val)
        cur = cur.next

    return nodes

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        return


class mySolution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # traverse list, remove previous node if duplicate encountered
        # use boolean val to determine if a duplicate was flagged

        dummy = ListNode(-500)
        dummy.next = head
        duplicated = False
        cur = head
        prev = dummy
        prev2 = dummy  # not necessary
        while cur is not None:
            if prev.val == cur.val:
                prev2.next = prev.next  # cur
                duplicated = True
            elif duplicated is True and prev.val != cur.val:
                prev2.next = prev.next
                duplicated = False
            else:
                prev2 = prev  # only advance prev2 if no deletion
            prev = cur
            cur = cur.next

        # remove final node if necessary
        if duplicated is True:
            prev2.next = None

        return dummy.next


class testcase1:
    head = [1, 2, 3, 3, 4, 4, 5]
    output = [1, 2, 5]
    linkedlisthead = build_linked_list(head)

class testcase2:
    head = [1, 1, 1, 2, 3]
    output = [2, 3]
    linkedlisthead = build_linked_list(head)

class testcase3:
    head = [1, 1, 1, 2, 2]
    output = []
    linkedlisthead = build_linked_list(head)

class testcase4:
    head = [1, 2, 3, 4, 4]
    output = [1, 2, 3]
    linkedlisthead = build_linked_list(head)

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.deleteDuplicates(testcase1.linkedlisthead)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    result2 = soln.deleteDuplicates(testcase2.linkedlisthead)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")

    # test example 3
    result3 = soln.deleteDuplicates(testcase3.linkedlisthead)
    listresult3 = linked_list_to_list(result3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {listresult3}, Correct: {listresult3 == testcase3.output}")

    # test example 4
    result4 = soln.deleteDuplicates(testcase4.linkedlisthead)
    listresult4 = linked_list_to_list(result4)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {listresult4}, Correct: {listresult4 == testcase4.output}")
