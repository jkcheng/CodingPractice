# 2095. Delete the Middle Node of a Linked List
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
#
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
#
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
#
#
# Example 1:
#
#
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node.
# Example 2:
#
#
# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.
# Example 3:
#
#
# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 105].
# 1 <= Node.val <= 105

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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        return


class mySolution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n), multiple passes: iterate list to count n nodes, then delete n/2th node
        # O(n), slow,fast pointer: delete node at slow when fast reachees end of list

        # slow,fast pointer
        slow, fast = head, head

        # iterate slow and fast pointers until end of list
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # delete slow from list
        prev.next = slow.next
        return dummy.next


class testcase1:
    head = [1,3,4,7,1,2,6]
    output = [1,3,4,1,2,6]

class testcase2:
    head = [1,2,3,4]
    output = [1,2,4]

class testcase3:
    head = [2,1]
    output = [2]

class testcase4:
    head = [10]
    output = []


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    linkedhead1 = build_linked_list(testcase1.head)
    result1 = soln.deleteMiddle(linkedhead1)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    linkedhead2 = build_linked_list(testcase2.head)
    result2 = soln.deleteMiddle(linkedhead2)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")

    # test example 3
    linkedhead3 = build_linked_list(testcase3.head)
    result3 = soln.deleteMiddle(linkedhead3)
    listresult3 = linked_list_to_list(result3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {listresult3}, Correct: {listresult3 == testcase3.output}")

    # test example 4
    linkedhead4 = build_linked_list(testcase4.head)
    result4 = soln.deleteMiddle(linkedhead4)
    listresult4 = linked_list_to_list(result4)
    print(f"Example 4 - Expected: {testcase4.output}, Got: {listresult4}, Correct: {listresult4 == testcase4.output}")