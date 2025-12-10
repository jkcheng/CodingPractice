# 2130. Maximum Twin Sum of a Linked List
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
#
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
#
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.
#
#
#
# Example 1:
#
#
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6.
# Example 2:
#
#
# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
# Example 3:
#
#
# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
#
#
# Constraints:
#
# The number of nodes in the list is an even integer in the range [2, 105].
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
        cur = cur.next

    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    nodes = []

    while head is not None:
        nodes.append(head.val)
        head = head.next

    return nodes

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        return


class mySolution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # O(1) space, O(2n) time: place first half nodes in stack and pop from stack when traversing second half

        # count nodes
        cur = head
        n = 0
        while cur is not None:
            n += 1
            cur = cur.next

        # add first half nodes to stack
        # pop from stack when traversing second half to update max twin sum
        stack = []
        cur = head
        count = 1
        maxsum = 0
        while cur is not None:
            # add nodes in first half to stack
            if count <= n // 2:
                stack.append(cur.val)
                count += 1
            # pop nodes from stack and update max sum
            else:
                val = stack.pop()
                maxsum = max(maxsum, val + cur.val)

            # move cur
            cur = cur.next

        return maxsum

class mySolution_reverse:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # O(n) time, O(1) space, reverse second half and traverse from both ends
        # 1-2-3-4-5-6-7-8

        # find halfway node with slow/fast pointers
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        cur = slow
        prev = None
        while cur is not None:
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode

        # find max twin sum
        # use head and prev as starts
        maxsum = 0
        while prev is not None and head is not None:
            maxsum = max(maxsum, prev.val + head.val)
            prev = prev.next
            head = head.next

        return maxsum


class testcase1:
    head = [5, 4, 2, 1]
    output = 6

class testcase2:
    head = [4, 2, 2, 3]
    output = 7

class testcase3:
    head = [1, 100000]
    output = 100001


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution_reverse()

    # test example 1
    linkedhead1 = build_linked_list(testcase1.head)
    result1 = soln.pairSum(linkedhead1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    linkedhead2 = build_linked_list(testcase2.head)
    result2 = soln.pairSum(linkedhead2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    linkedhead3 = build_linked_list(testcase3.head)
    result3 = soln.pairSum(linkedhead3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")
