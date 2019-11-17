# https://leetcode.com/problems/permutations-ii/

# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = itertools.permutations(nums)
        return set(res)