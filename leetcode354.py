# 354. Russian Doll Envelopes
# Hard
# Topics
# Companies
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
#
# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.
#
# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
#
# Note: You cannot rotate an envelope.
#
#
#
# Example 1:
#
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# Example 2:
#
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
#
#
# Constraints:
#
# 1 <= envelopes.length <= 105
# envelopes[i].length == 2
# 1 <= wi, hi <= 105

# https://leetcode.com/problems/russian-doll-envelopes/solutions/82761/python-o-nlogn-o-n-solution-beats-97-with-explanation
# https://leetcode.com/problems/russian-doll-envelopes/solutions/1134197/python-4-lines-solution-explained

from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        return


class mySolution:
    # similar to leetcode300: longest increasing subsequence
    # sort envelopes by increasing width, with heights decreasing for envelopes of same width (e.g. [[1,2],[3,5],[3,4]]
    # find longest increasing subsequence of heights
    # having heights in reverse order ensures finding LIS of heights won't result in invalid envelope sequences with same width like [3,4][3,5]
    # O(nlogn): sort envelopes by width (secondary sort height in reverse order), find LIS of heights by binary search
    # If next envelope has larger height than previous, append to LIS and extend length
    # If next envelope is *not* larger height, then binary search to find smallest height bigger than this next envelope
    # Replace old nesting envelope with this new next envelope to build a new LIS chain
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def binsearch_idx(lis, e):
            l, r = 0, len(lis)-1

            idx = None
            while l <= r:
                mid = (l+r)//2
                if lis[mid][1] >= e[1]:
                    idx = mid
                    r = mid-1
                else:
                    l = mid+1

            return idx

        lis = []
        # sort envelopes by increasing width, decreasing height
        envelopes = sorted(envelopes, key=lambda x: [x[0], -x[1]])
        for e in envelopes:
            # if envelope height bigger than previous, append and extend LIS
            if len(lis) == 0 or e[1] > lis[-1][1]:
                lis.append(e)
            # binary search to find envelope to replace
            else:
                idx = binsearch_idx(lis, e)
                lis[idx] = e

        return len(lis)


class testcase1:
    envelopes = [[5,4],[6,4],[6,7],[2,3]]

class testcase2:
    envelopes = [[1,1],[1,1],[1,1]]

# class testcase3:
#     nums = [7,7,7,7,7,7,7]
#
# class testcase4:
#     nums = [14,4,6,