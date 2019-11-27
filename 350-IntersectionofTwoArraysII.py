# https://leetcode.com/problems/intersection-of-two-arrays-ii/

# Given two arrays, write a function to compute their intersection.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        n1, n2 = collections.Counter(nums1), collections.Counter(nums2)
        for c in n1:
            if c in n2:
                for i in range(min(n1[c], n2[c])):
                    res.append(c)
        return res