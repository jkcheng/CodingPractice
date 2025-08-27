# 23. Merge k Sorted Lists
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#
#
# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:
#
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []
#
#
# Constraints:
#
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

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
    listvals = []
    while head is not None:
        listvals.append(head.val)
        head = head.next

    return listvals

# idea: repeatedly merge pairs of linked-lists in the lists of lists. This will be O(nlogk) time where k is the number of linked-lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                merged.append(self.mergeLists(l1, l2))

            lists = merged

        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next


class mySolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. use heap (priority queue) to store nodes from each of k lists
        # repeatedly pushpop nodes into heap to get smallest node among k lists and add to result
        # 2. recursively (or iteratively) merge two single lists together
        # all O(nlogk) time
        # divide and conquer, recursive merge sort

        # two-pointer merge sort
        def mergeLists(head1, head2):
            # todo: maybe change input structure to just linked lists
            # head1 = lists1[0]
            # head2 = lists2[0]

            dummy = ListNode(-1)
            cur = dummy
            while head1 is not None and head2 is not None:
                if head1.val <= head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next

            # add the remaining list
            if head1 is not None:
                cur.next = head1
            else:
                cur.next = head2

            return dummy.next

        # base case: no lists
        if len(lists) == 0:
            return None

        # base case: one single list
        if len(lists) == 1:
            return lists[0]  # return head of single linked list

        # split set of lists into two halves
        mid = len(lists) // 2  # mid will be index of first item in second set

        lists1 = lists[0:mid]
        lists2 = lists[mid:]

        merged1 = self.mergeKLists(lists1)
        merged2 = self.mergeKLists(lists2)

        # return merge sort
        return mergeLists(merged1, merged2)


class testcase1:
    lists = [[1,4,5],[1,3,4],[2,6]]
    output = [1,1,2,3,4,4,5,6]
    listheads = [build_linked_list(l) for l in lists]

class testcase2:
    lists = []
    output = []
    listheads = [build_linked_list(l) for l in lists]

class testcase3:
    lists = [[]]
    output = []
    listheads = [build_linked_list(l) for l in lists]


if __name__ == '__main__':
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.mergeKLists(testcase1.listheads)
    listresult1 = linked_list_to_list(result1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {listresult1}, Correct: {listresult1 == testcase1.output}")

    # test example 2
    result2 = soln.mergeKLists(testcase2.listheads)
    listresult2 = linked_list_to_list(result2)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {listresult2}, Correct: {listresult2 == testcase2.output}")

    # test example 3
    result3 = soln.mergeKLists(testcase3.listheads)
    listresult3 = linked_list_to_list(result3)
    print(f"Example 3 - Expected: {testcase3.output}, Got: {listresult3}, Correct: {listresult3 == testcase3.output}")

