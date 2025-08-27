# 2. Add Two Numbers
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
#
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
# Constraints:
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(head: List) -> ListNode:
    if not head:
        return None

    dummy = ListNode(0)
    node = dummy
    for n in head:
        nextnode = ListNode(n)
        node.next = nextnode
        node = nextnode

    return dummy.next

def convert_linked_list_to_array(head: ListNode) -> List[int]:
    res = []
    if not head:
        return res

    while head:
        res.append(head.val)
        head = head.next
    return res


# idea: traverse lists and multiply by powers of 10 before adding
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        dummy = ListNode(-1)
        node = dummy
        carry = 0

        while cur1 or cur2 or carry == 1:

            if cur1:
                val1 = cur1.val
            else:
                val1 = 0

            if cur2:
                val2 = cur2.val
            else:
                val2 = 0

            num = val1 + val2 + carry
            nodeval = num%10
            if num >= 10:
                carry = 1
            else:
                carry = 0

            nextnode = ListNode(nodeval)
            node.next = nextnode
            node = nextnode
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        return dummy.next

class mySolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # manually add each digit one at a time
        # cannot convert number to int because number may exceed 32-bit int
        # create dummy pointer
        dummy = ListNode(0)
        cur = dummy

        carry = 0
        while l1 is not None or l2 is not None:
            # add integers
            n1 = l1.val if l1 is not None else 0
            n2 = l2.val if l2 is not None else 0
            res = n1+n2+carry

            # handle carrying values
            if res >= 10:
                carry = 1
                res = res % 10 # set result to modulo
            else:
                carry = 0

            # set result as node
            resnode = ListNode(res)
            cur.next = resnode
            cur = resnode

            # move pointers
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # add extra node if carry remains (can also add "or carry==1" to while loop condition)
        if carry == 1:
            carrynode = ListNode(carry)
            cur.next = carrynode
            # cur = cur.next # not necessary

        return dummy.next


class testcase1:
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    output = [7,0,8]

class testcase2:
    l1 = [0]
    l2 = [0]
    output = [0]

class testcase3:
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    output = [8,9,9,9,0,0,0,1]

if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    l1linked = build_linked_list(testcase1.l1)
    l2linked = build_linked_list(testcase1.l2)
    result1linked = soln.addTwoNumbers(l1linked, l2linked)
    result1 = convert_linked_list_to_array(result1linked)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    l1linked = build_linked_list(testcase2.l1)
    l2linked = build_linked_list(testcase2.l2)
    result2linked = soln.addTwoNumbers(l1linked, l2linked)
    result2 = convert_linked_list_to_array(result2linked)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    l1linked = build_linked_list(testcase3.l1)
    l2linked = build_linked_list(testcase3.l2)
    result3linked = soln.addTwoNumbers(l1linked, l2linked)
    result3 = convert_linked_list_to_array(result3linked)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {result3}, Correct: {result3 == testcase3.output}")

