# https://leetcode.com/contest/weekly-contest-241/problems/sum-of-all-subset-xor-totals/

# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if
# the array is empty.

#     For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.

# Given an array nums, return the sum of all XOR totals for every subset of nums.

# Note: Subsets with the same elements should be counted multiple times.

# An array a is a subset of an array b if a can be obtained from b by deleting some
# (possibly zero) elements of b.

from itertools import combinations


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(1, len(nums) + 1):
            for combo in combinations(nums, i):
                if len(combo) == 1:
                    res += combo[0]
                elif len(combo) == 2:
                    res += combo[0] ^ combo[1]
                else:
                    local_res = combo[0] ^ combo[1]
                    j = 2
                    while j < len(combo):
                        local_res = local_res ^ combo[j]
                        j += 1
                    res += local_res
        return res
