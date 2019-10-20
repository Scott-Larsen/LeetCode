# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once. Find
# this single element that appears only once.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        while end - start > 2:
            mid = (start + end) // 2
            if mid % 2 == 1 and mid != 2:
                mid += 1
            if nums[mid - 2] != nums[mid - 1]:
                end = mid
            else:
                start = mid
        return nums[start]