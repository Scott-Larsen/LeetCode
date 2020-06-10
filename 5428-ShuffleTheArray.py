# https://leetcode.com/contest/weekly-contest-192/problems/shuffle-the-array/

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        nums1, nums2 = nums[:n], nums[n:]
        while nums1:
            res.append(nums1.pop(0))
            res.append(nums2.pop(0))
        return res