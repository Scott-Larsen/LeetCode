# Given a set of distinct integers, nums, return all possible subsets (the power
# set).

# Note: The solution set must not contain duplicate subsets.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for num in nums:
            ret += [r + [num] for r in ret]
        return ret