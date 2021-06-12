# https://leetcode.com/contest/weekly-contest-244/problems/reduction-operations-to-make-the-array-elements-equal/

# Given an integer array nums, your goal is to make all elements in nums equal. To
# complete one operation, follow these steps:

#     Find the largest value in nums. Let its index be i (0-indexed) and its value be
#     largest. If there are multiple elements with the largest value, pick the smallest i.
#     Find the next largest value in nums strictly smaller than largest. Let its value be
#     nextLargest.
#     Reduce nums[i] to nextLargest.

# Return the number of operations to make all elements in nums equal.


from collections import defaultdict


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        d = defaultdict(int)
        s = set()
        for num in nums:
            d[num] += 1
            s.add(num)
        l = sorted(list(s), reverse=True)
        res = 0
        sum = 0
        for n in l[:-1]:
            sum += d[n]
            res += sum
        return res
