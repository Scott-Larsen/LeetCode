# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/submissions/

# Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

# Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.
 
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        print(nums)
        # print(nums[len(nums) - 4], nums[0], nums[-1], nums[3])
        minimum = 99999999999999
        difference = len(nums) - 3
        for i in range(len(nums) - difference + 1):
            print(nums[i + difference - 1], nums[i])
            minimum = min(minimum, nums[i + difference - 1] - nums[i])
        return minimum