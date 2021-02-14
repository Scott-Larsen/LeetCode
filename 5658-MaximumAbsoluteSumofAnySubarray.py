# 5658. Maximum Absolute Sum of Any Subarray

# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

#     If x is a negative integer, then abs(x) = -x.
#     If x is a non-negative integer, then abs(x) = x.


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxCurrent = maxRes = minCurrent = minRes = 0
        for _, v in enumerate(nums):
            maxCurrent = max(v, maxCurrent + v)
            maxRes = max(maxRes, maxCurrent)
            minCurrent = min(v, minCurrent + v)
            minRes = min(minRes, minCurrent)
        return max(maxRes, abs(minRes))
