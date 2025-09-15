# 295. Find Median from Data Stream
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
#
#
# Example 1:
#
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
#
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#
#
# Constraints:
#
# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
#
#
# Follow up:
#
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

from typing import List, Optional
import inspect

import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        return

    def addNum(self, num: int) -> None:
        # add to appropriate heap
        if self.minheap and num >= self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)

        # balance heaps
        if (len(self.minheap) - len(self.maxheap)) > 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)
        elif (len(self.maxheap) - len(self.minheap)) > 1:
            val = heapq.heappop(self.maxheap)  # a negative value
            heapq.heappush(self.minheap, -val)

        return

    def findMedian(self) -> float:
        # median = None
        if len(self.minheap) > len(self.maxheap):
            median = self.minheap[0]
        elif len(self.maxheap) > len(self.minheap):
            median = -self.maxheap[0]
        else:
            median = (self.minheap[0] + (-self.maxheap[0])) / 2

        return median

import heapq
class myMedianFinder:
    # maintain a min and max heap both containing n/2 items
    # add new num to appropriate heap, then rebalance heap sizes
    def __init__(self):
        self.minheap = []  # contains larger half values
        self.maxheap = []  # contains smaller half values

    def addNum(self, num: int) -> None:
        if len(self.minheap) > 0 and num >= self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:  # num <= self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)

        # rebalance heap sizes
        while abs(len(self.minheap) - len(self.maxheap)) > 1:
            if len(self.minheap) - len(self.maxheap) > 1:
                val = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -val)
            elif len(self.maxheap) - len(self.minheap) > 1:
                val = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -val)

    def findMedian(self) -> float:
        # get value from the top of the heap with larger size
        if len(self.minheap) > len(self.maxheap):
            ans = self.minheap[0]
        elif len(self.maxheap) > len(self.minheap):
            ans = -self.maxheap[0]
        else:
            ans = (self.minheap[0] - self.maxheap[0]) / 2

        return ans

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class testcase1:
    input = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    inputvals = [[], [1], [2], [], [3], []]
    output = [None, None, None, 1.5, None, 2.0]


if __name__ == "__main__":
    # create class instance
    finder = myMedianFinder()

    # helper function to test
    def test_soln(testcase):
        output = []
        for input, vals in zip(testcase.input, testcase.inputvals):
            methods = inspect.getmembers(finder, predicate=inspect.ismethod)
            for method_name, method in methods:
                if method_name == input:
                    res = method(vals[0] if len(vals) > 0 else None)
                    output.append(res)

        return output

    # test example 1
    result1 = test_soln(testcase1)
    print(f"Example 1 - Expected: {testcase1.output}, Got: {result1}, Correct: {testcase1.output == result1}")


