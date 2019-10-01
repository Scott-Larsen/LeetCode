# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dups.append(abs(num))
            else:
                nums[abs(num) - 1] = -nums[abs(num) - 1]
        return dups