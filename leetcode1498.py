from typing import List
class Solution:
    # solution link
    # https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/solutions/986887/python3-sort-binary-search-count-subsets
    # discussion on subsequence
    # https://math.stackexchange.com/questions/23513/why-is-the-number-of-possible-subsequences-2n
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        ct = 0

        n = len(nums)
        nums.sort()

        def bsearch(x: List[int], t: int, l: int, n: int = n) -> int:
            # Returns the rightmost valid index for number <= target
            r = n - 1
            while (l < r):
                m = l + (r - l) // 2 + 1
                if x[m] <= t:
                    l = m
                else:
                    r = m - 1
            return r

        # loop on min value
        for i in range(n):
            if 2 * nums[i] > target:
                # no need to process further (sorted array)
                break

                # find max j for valid subarray
            j = bsearch(nums, target - nums[i], i)
            if nums[i] + nums[j] <= target:
                # add 1 * 2^((j - i + 1) - 1) for no. of subsets
                # from subarray with one element fixed
                ct += pow(2, j - i, mod)  # for efficient handling of large no.s
        return ct % mod


class mySolution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # O(nlogn): sort, then binary search
        # the total number of subsequences in a given array of length n is 2**n, inclusive of the empty set []
        # [3,6,5,7]
        # [3,5,6,7]
        # because we are only concerned counting subsequence with valid max+min (and not returning the unique subsequences themselves),
        # we can safely sort and do the counting on the sorted array and get the same answer
        # thus the solution can be modified to be:
        # for each n in sorted(nums), find the largest subarray where max+n <= target
        # add the number of subsequences that can be constructed with this subarray from [n,max_value]
        # repeat for each n in sorted(nums) to find all the subsequences that are valid

        # binary search to find largest bound for subarray
        def binsearch(nums, i, j):
            l, r = i, j
            maxright = None
            while l <= r:
                mid = (l + r) // 2
                # note valid maxright and search right
                if nums[mid] + nums[i] <= target:
                    if maxright == None:
                        maxright = mid
                    else:
                        maxright = max(maxright, mid)
                    l = mid + 1
                else:
                    r = mid - 1

            # return max index of valid subarray starting at i
            return maxright

        # sort array
        nums = sorted(nums)
        mod = (10 ** 9 + 7)
        ans = 0
        for i in range(len(nums)):
            if nums[i]*2 > target:
                break # rest of array can't form valid subsequences

            maxright = binsearch(nums, i, len(nums)-1)

            # count of valid subsequences that MUST include nums[i]
            # apply % mod for speed gain while cumulating sum, doesn't change solution?
            # subseqcount = 2**(maxright-i) # % mod
            subseqcount = pow(2, maxright - i) % mod
            # print('ans:', ans)
            # print('subseqcount:', subseqcount)
            ans += subseqcount

        # print('maxright:', maxright)
        # print('modulo:', mod)
        # print('pow:', subseqcount)
        # print('pow%mod:', subseqcount % mod)
        # print('ans before mod:', ans)
        return ans%mod # required for correct answer, even if mod is applied in loop

class testcase1:
    nums = [3,5,6,7]
    target = 9

class testcase2:
    nums = [3,3,6,8]
    target = 10

class testcase3:
    nums = [2,3,3,4,6,7]
    target = 12

class testcase4:
    nums = [14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14]
    target = 22

### case examples for testcase 2:
# # including first "3": 2**(3-1)
# [3,3]
# [3,3,6]
# [3,6]
# [3]
#
# # second "3"
# [3]
# [3,6]
#
# # all possible subseq of [3,3,6]: 2**3
# []
# [3]
# [3,3]
# [3,3,6]
# [3,6]
# [3]
# [3,6]
# [6] ## invalid subseq!