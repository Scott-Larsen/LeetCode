# 1755. Closest Subsequence Sum

# You are given an integer array nums and an integer goal.

# You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

# Return the minimum possible value of abs(sum - goal).

# Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

from itertools import combinations


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        half = len(nums) // 2
        left, right = nums[:half], nums[half:]
        leftCombos, rightCombos = set(), set()

        def comboSums(n, s):
            for i in range(1, len(n) + 1):
                combos = combinations(n, i)
                for combo in combos:
                    s.add(sum(combo))
            return s

        leftCombos, rightCombos = comboSums(left, leftCombos), comboSums(
            right, rightCombos
        )
        leftCombos.add(0)
        rightCombos.add(0)
        rightCombos = sorted(list(rightCombos))

        res = abs(goal)
        for _, v in enumerate(leftCombos):
            r = bisect_left(rightCombos, goal - v)
            len_ = len(rightCombos)
            if r < len_:
                res = min(res, abs(v + rightCombos[r] - goal))
            if r > 0:
                res = min(res, abs(v + rightCombos[r - 1] - goal))
        return res