# 25. Reverse Nodes in k-Group
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
#
# Constraints:
#
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
#
#
# Follow-up: Can you solve the problem in O(1) extra memory space?

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
    nodes = []
    if head is None:
        return nodes

    cur = head
    while cur:
        nodes.append(cur.val)
        cur = cur.next

    return nodes

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prevgroup = dummy
        first = True

        while True:
            # get last node of group and first node of next group
            kth = self.getKthNode(prevgroup, k)
            if not kth:
                break
                # pass
            nextgroup = kth.next

            # reverse k nodes
            cur = prevgroup.next
            prev = nextgroup
            while cur and cur != nextgroup:
                nextnode = cur.next
                cur.next = prev
                prev = cur
                cur = nextnode

            tmp = prevgroup.next  # store last node in newly reversed group
            prevgroup.next = kth  # set last node of prevgroup to point to first node of newly reversed group
            prevgroup = tmp  # set prevgroup to end of newly reversed group
            if first:
                dummy.next = prev
                first = False

        return dummy.next

    def getKthNode(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        cur = node
        while count < k and cur:
            cur = cur.next
            count += 1

        return cur

class mySolution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find k nodes that need reversing, reverse k nodes and connect to original
        # check if >k nodes remain that need to be reversed
        # repeat

        aftergroup = None
        dummy = ListNode(-1)
        dummy.next = head

        beforegroup = dummy
        while True:
            # move k nodes forward, return kth node
            # aftergroup = kth.next
            # reverse(k_nodes)

            # reassign beforegroup and aftergroup pointers
            # first = beforegroup.next
            # last = kth
            # beforegroup.next = last
            # first.next = aftergroup
            # if this is first group reversed, dummy.next = last

            # get kth node
            cur = beforegroup
            for _ in range(k):
                if cur is not None:
                    cur = cur.next

            # stop reversing if cur falls off list
            if cur is None:
                break

            # reverse k nodes, cur at kth node
            aftergroup = cur.next # could be None
            before = aftergroup  # set initial before node to aftergroup
            cur = beforegroup.next  # reset cur to start of group to reverse
            # while cur is not None and cur != aftergroup:
            while cur != aftergroup:
                after = cur.next
                cur.next = before  # will set initially next to aftergroup
                before = cur
                cur = after

            firstreversed = beforegroup.next # first node of the reversed group (before reversing)
            beforegroup.next = before  # before is last node of reversed group (before reversing)
            # firstreversed.next = aftergroup # not necessary? handled in loop
            beforegroup = firstreversed  # set to last node of reversed group

        return dummy.next

class testcase1:
    head = [1, 2, 3, 4, 5]
    k = 2
    output = [2, 1, 4, 3, 5]
    linkedlisthead = build_linked_list(head)

class testcase2:
    head = [1, 2, 3, 4, 5]
    k = 3
    output = [3, 2, 1, 4, 5]
    linkedlisthead = build_linked_list(head)

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.reverseKGroup(testcase1.linkedlisthead, testcase1.k)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    result2 = soln.reverseKGroup(testcase2.linkedlisthead, testcase2.k)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")
