#  Given an unsorted array of integers, find the length of longest continuous
#  increasing subsequence (subarray). 

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 1 if len(nums) > 0 else 0        
        for i in range(len(nums)):
            start = nums[i]
            current = nums[i]
            long = 1
            for j in range(1, len(nums) - i):
                if nums[i + j] > start and nums[i + j] > current:
                    current = nums[i + j]
                    long += 1
                    if long > longest:
                        longest = long
                else:
                    break
        return longest