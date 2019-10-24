# Given a collection of integers that might contain duplicates, nums, return all
# possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for num in sorted(nums):
            ret += [[num] + r for r in ret if [num] + r not in ret]
        return ret