# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n + 1)]
        return combinations(arr, k)