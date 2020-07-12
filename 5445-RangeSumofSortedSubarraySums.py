# https://leetcode.com/contest/biweekly-contest-30/problems/range-sum-of-sorted-subarray-sums/

# Given the array nums consisting of n positive integers. You computed the sum of all non-empty continous subarrays from the array and then sort them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

# Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 10^9 + 7.

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(len(nums)):
            current_sum = 0
            for j in range(len(nums) - i):
                current_sum += nums[i + j]
                sums.append(current_sum)
        sums.sort()
        return sum(sums[left - 1: right])