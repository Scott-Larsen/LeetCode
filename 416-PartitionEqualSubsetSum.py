# https://leetcode.com/problems/partition-equal-subset-sum/

# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        other = []
        # sort.nums()
        target = sum(nums)
        if target % 2 != 0:
            return False
        else:
            target /= 2
        for i in range(len(nums) * 500):
            # This randint is hacky but it works
            if sum(nums) > target:
                num = random.randint(0, len(nums) - 1)
                other = [nums.pop(num)] + other
            elif sum(nums) < target:
                num = random.randint(0, len(other) - 1)
                nums = [other.pop(num)] + nums
            else:
                return True
        return False