# 528. Random Pick with Weight
# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
#
# You need to implement the function pickIndex(), which randomly picks an index in the range
# [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
#
# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%),
# and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
from typing import List
import random
class Solution:

    def __init__(self, w: List[int]):
        s = sum(w)
        self.weight = [w[0]/s]
        for i in range(1, len(w)):
            self.weight.append(self.weight[-1]+w[i]/s)

    def pickIndex(self) -> int:
        l = 0
        r = len(self.weight)-1
        seed = random.random()

        while l < r:
            m = (l+r)//2
            if seed < self.weight[m]:
                r = m
            else:
                l = m + 1
        return l


# practice
# O(logn): create array x of length w in the range [0,1] where x[i] = cumulative weights of all values x[0] to x[i]
# e.g.: for w = [1,3,6], x = [0.1,0.4,1]
# use random.random() to generate a number in the range [0,1] and use binary search to find smallest i where
# x[i] >= w[i]/sum(w) (individual weight of w[i])

class mySolution:
    def __init__(self, w: List[int]):
        # build array of cumulative probs
        total = sum(w)
        self.probs = []
        self.probs.append(w[0]/total)
        for i in range(1,len(w)):
            cumulative_prob = self.probs[-1] + (w[i]/total)
            self.probs.append(cumulative_prob)

        print(self.probs)


    def pickIndex(self) -> int:
        # random generate float, binary search through cumulative weights index
        l, r = 0, len(self.probs)-1

        randval = random.random()
        minidx = len(self.probs)
        while l <= r:
            mid = (l+r)//2
            if self.probs[mid] >= randval:
                minidx = min(minidx, mid)
                r = mid-1
            else:
                l = mid+1

        return minidx


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

class testcase1:
    cases = ["Solution","pickIndex"]
    input = [[[1]],[]]

class testcase2:
    cases = ["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"]
    input = [[[1,3]],[],[],[],[],[]]

class testcase3:
    cases = ["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex","pickIndex","pickIndex","pickIndex"]
    input = [[[1,3,6]],[],[],[],[],[],[],[],[]]
#
# class testcase4:
#     nums = [14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14]
#     target = 22