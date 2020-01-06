# https://leetcode.com/problems/maximum-product-of-three-numbers/

# Given an integer array, find three numbers whose product is maximum and output
# the maximum product.

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0] * nums[1]
        b = nums[-1] * nums[-2]
        return max([a * nums[-1], b * nums[-3]])