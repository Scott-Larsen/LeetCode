# 5657. Sum of Unique Elements

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.


from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        res = 0
        c = Counter(nums)
        for num in c.keys():
            if c[num] == 1:
                res += num
        return res
