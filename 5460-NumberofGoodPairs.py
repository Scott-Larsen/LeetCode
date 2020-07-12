# https://leetcode.com/contest/weekly-contest-197/problems/number-of-good-pairs/

# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        p = itertools.combinations(nums, 2)
        for combo in p:
            if combo[0] == combo[1]:
                res += 1
        return res