# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = sorted(nums)
        l, r = 0, len(nums) - 1
        while l < len(nums):
            if nums[l] == n[l]:
                l += 1
            else:
                break
        if l == len(nums):
            return 0
        while r > 0:
            if nums[r] == n[r]:
                r -= 1
            else:
                break
        return r - l + 1