# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it
# without using extra memory?

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) -1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]
        
#         while len(nums) > 1:
#             n = nums.pop()
#             if n in nums:
#                 nums.remove(n)
#             else:
#                 return n
#         return nums[0]
    
    
#         for num in nums:
#             if nums.count(num) == 1:
#                 return num