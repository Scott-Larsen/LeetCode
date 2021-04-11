# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Given an array of integers that is already sorted in ascending order, find two
# numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num in (sorted(set(numbers))):
            firstIndex = numbers.index(num)
            remaining = numbers[firstIndex + 1:]        
            if (target - num) in remaining:
                secondIndex = firstIndex + remaining.index(target - num) + 1
                return [firstIndex + 1, secondIndex + 1]