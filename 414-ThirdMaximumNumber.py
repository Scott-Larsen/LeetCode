# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(list(nums))
        else:
            nums = list(set(nums))
            nums.sort()
            return nums[-3]