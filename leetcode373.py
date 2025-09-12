# 373. Find K Pairs with Smallest Sums
# Medium
# Topics
# premium lock icon
# Companies
# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
#
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
#
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.
#
#
#
# Example 1:
#
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:
#
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
#
# Constraints:
#
# 1 <= nums1.length, nums2.length <= 105
# -109 <= nums1[i], nums2[i] <= 109
# nums1 and nums2 both are sorted in non-decreasing order.
# 1 <= k <= 104
# k <= nums1.length * nums2.length

from typing import List, Optional


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:


        return

import heapq
class mySolution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # similar to merge k-sorted lists
        # treat each pairing (nums1[i], nums2[j]) as a series of linked lists (or series)
        # each list has a fixed i and j ranges from [0,len(nums2)]. e.g. (nums1[0],nums2[0]),(nums1[0],nums2[1]),etc..
        # maintain a heap of size k, with each smallest sum pair popped replaced with the next pair in that "series"
        # e.g. if (nums1[0],nums2[3]) popped, replace with (nums1[0],nums2[4])
        # since we only care about the smallest k, initially considering only the first k items from nums1 is ok
        heap = []
        for i in range(min(k, len(nums1))):
            pair = (i, 0)  # indices of nums1,nums2 pairs
            sumval = nums1[i] + nums2[0]
            heap.append((sumval, pair))

        heapq.heapify(heap)

        res = []
        while k > 0:
            sumval, pair = heapq.heappop(heap)
            i = pair[0]
            j = pair[1]
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                newsumval = nums1[i] + nums2[j + 1]
                newpair = (i, j + 1)
                heapq.heappush(heap, (newsumval, newpair))
            k -= 1

        return res

class testcase1:
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    output = [[1,2],[1,4],[1,6]]

class testcase2:
    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 2
    output = [[1,1],[1,1]]


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution()

    # test example 1
    result1 = soln.kSmallestPairs(testcase1.nums1, testcase1.nums2, testcase1.k)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")

    # test example 2
    result2 = soln.kSmallestPairs(testcase2.nums1, testcase2.nums2, testcase2.k)
    print(f"Example 2 - Expected: {testcase2.output}, Got: {result2}, Correct: {testcase2.output == result2}")