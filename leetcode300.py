# 300. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing
# subsequence
#
#
#
# Example 1:
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104

# https://leetcode.com/problems/longest-increasing-subsequence/solutions/429079/python-5-approaches-recursion-recur-memo-dp-dp-binary-search-print-all-lis
# https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326552/optimization-from-brute-force-to-dynamic-programming-explained
# https://leetcode.com/problems/longest-increasing-subsequence/solutions/667975/python-3-lines-dp-with-binary-search-explained
# best explanation of nlogn solution:
# https://leetcode.com/problems/longest-increasing-subsequence/solutions/74824/java-python-binary-search-o-nlogn-time-with-explanation

from typing import List

class Solution:
    # 1D DP O(n^2): maintain dp array where dp[i] is the LIS (longest increasing subsequence) STARTING at nums[i]
    # e.g. for nums3 = [0,1,0,3,2,3], dp[5] == 1 ([3] is LIS), dp[4] == 2 ([2,3]), dp[3] == 1 ([3])
    # build dp array backwards starting at end of nums, with dp[i] = max(1,1+rest_of_dp_array)
    class Solution:
        def lengthOfLIS(self, nums: List[int]) -> int:
            length = len(nums)
            dp = [1] * length
            for i in reversed(range(length - 1)):
                for j in range(i + 1, length):
                    # take the max value of 1 and 1+dp[i+1], 1+dp[i+2], etc. if nums[i+x] > n
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[i],
                                    1 + dp[j])  # since we're iterating we need to get the max of dp[i] vs 1+dp[j]
            return max(dp)  # return longest LIS in dp array

class mySolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # # O(2^n): recursive approach, check every possible subsequence and note length of LIS from each n in nums
        # #
        # def lis_at_index(prev, i, nums):
        #     LIS_include, LIS_exclude = 0, 0
        #     # base case: end of nums array
        #     if i == len(nums):
        #         return LIS_exclude
        #
        #     # get LIS for including current value at i if valid
        #     if nums[i] > prev:
        #         LIS_include = 1 + lis_at_index(nums[i], i+1, nums)
        #
        #     # get LIS for excluding current value
        #     LIS_exclude = lis_at_index(prev, i+1, nums)
        #     return max(LIS_exclude, LIS_include)

        # O(n^2): improvement using memoization by iterating backwards
        memo = [0]*len(nums)

        for i in reversed(range(len(nums))):
            LIS_include, LIS_exclude = 0, 0
            prev = nums[i+1] if i+1 < len(nums) else float('inf')
            # LIS including current i
            if nums[i] < prev:
                if i+1 < len(nums):
                    LIS_include = 1 + memo[i+1]
                else:
                    LIS_include = 1 + 0
            # LIS excluding current i
            LIS_exclude = memo[i+1] if i+1 < len(nums) else 0
            memo[i] = max(LIS_include, LIS_exclude)


        return memo[0]

class mySolution2:
    # O(nlogn): binary search, build LIS by scanning array left to right.
    # If next encountered element is larger than last element in LIS, then append to LIS and extend length
    # If element is *not* larger tha last element in LIS, then binary search in LIS to find smallest element LARGER than current element
    # This trick allows for tracking multiple LIS using one array
    # It does not form a valid LIS, but the length is correct.
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binsearch_idx(lis, n):
            l, r = 0, len(lis)-1

            idx = None
            while l <= r:
                mid = (l+r)//2
                if lis[mid] >= n:
                    idx = mid
                    r = mid-1
                else:
                    l = mid+1

            return idx

        lis = []
        for n in nums:
            # append n and extend lis if n is larger than last element in candidate lis
            if len(lis) == 0 or n > lis[-1]:
                lis.append(n)
            else:
                # binary search to find smallest element in lis larger than n and replace
                idx = binsearch_idx(lis, n)
                lis[idx] = n

        return len(lis)

class mySolution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n^2): 1d dp, create dp array where dp[i] = LIS using this number
        # dp[i] = 1+dp[j], where j = index of largest LIS to the left and nums[j] < nums[i]

        # O(n^2) solution
        dp = [1]*len(nums)

        longest = 1
        for i in range(1,len(dp)):
            elligible = [(n,lis) for n,lis in zip(nums[0:i],dp[0:i]) if n < nums[i]]
            if len(elligible) > 0:
                longest_elligible = max(elligible, key=lambda x: x[1])
                dp[i] = 1+longest_elligible[1]
                longest = max(longest, dp[i])


        return longest


class testcase1:
    nums = [10,9,2,5,3,7,101,18]
    output = 4

class testcase2:
    nums = [0,1,0,3,2,3]
    output = 4

class testcase3:
    nums = [7,7,7,7,7,7,7]
    output = 1

class testcase4:
    nums = [14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14]
    output = 11


if __name__ == "__main__":
    # create Solution instance
    soln = mySolution3()

    # test example 1
    result1 = soln.lengthOfLIS(testcase1.nums)
    print(f"Example 1 - Expected: {len(testcase1.nums)}, Got: {result1}, Correct: {result1 == testcase1.output}")

    # test example 2
    result2 = soln.lengthOfLIS(testcase2.nums)
    print(f"Example 2 - Expected: {len(testcase2.nums)}, Got: {result2}, Correct: {result2 == testcase2.output}")

    # test example 3
    result3 = soln.lengthOfLIS(testcase3.nums)
    print(f"Example 3 - Expected: {len(testcase3.nums)}, Got: {result3}, Correct: {result3 == testcase3.output}")

    # test example 4
    result4 = soln.lengthOfLIS(testcase4.nums)
    print(f"Example 4 - Expected: {len(testcase4.nums)}, Got: {result4}, Correct: {result4 == testcase4.output}")