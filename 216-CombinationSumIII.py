# https://leetcode.com/problems/combination-sum-iii/

# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        for c in itertools.combinations(range(1,10), k):
            if sum(c) == n:
                res.append(c)
        return res