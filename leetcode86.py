# 86. Partition List
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before
# nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
#
#
# Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
# Example 2:
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        return


class mySolution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # O(n): traverse list and maintain pointer to last node < x
        # move any node < x afterward to this pointer and increment pointer

        dummy = ListNode(-1000)
        dummy.next = head
        prev = dummy
        cur = dummy
        # move last to last node < x and cur the next node
        while cur is not None and cur.val < x:
            prev = cur
            cur = cur.next

        curprev = prev
        while cur is not None:
            # check if node needs swapping
            if cur.val < x:
                prevnext = prev.next
                curnext = cur.next
                prev.next = cur
                cur.next = prevnext
                curprev.next = curnext

                # advance pointers
                prev = cur
                cur = curnext

            else:
                # advance cur
                curprev = cur
                cur = cur.next

        return dummy.next

class testcase1:
    head = [1, 4, 3, 2, 5, 2]
    x = 3
    output = [1, 2, 2, 4, 3, 5]
    linkedlisthead = build_linked_list(head)

class testcase2:
    head = [2, 1]
    x = 2
    output = [1, 2]
    linkedlisthead = build_linked_list(head)

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.partition(testcase1.linkedlisthead, testcase1.x)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    result2 = soln.partition(testcase2.linkedlisthead, testcase2.x)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")
