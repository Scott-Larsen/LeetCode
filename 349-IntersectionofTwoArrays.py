# Given two arrays, write a function to compute their intersection.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = set(nums1), set(nums2)
        return [n for n in n1 if n in n2]