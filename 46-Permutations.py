# Given a collection of distinct integers, return all possible permutations.

from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return (permutations(nums, len(nums)))