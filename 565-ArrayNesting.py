# https://leetcode.com/problems/array-nesting/

# A zero-indexed array A of length N contains all integers from 0 to N-1. Find
# and return the longest length of set S, where S[i] = {A[i], A[A[i]],
# A[A[A[i]]], ... } subjected to the rule below.

# Suppose the first element in S starts with the selection of element A[i] of
# index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By
# that analogy, we stop adding right before a duplicate element occurs in S.

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            count = 0
            while nums[i] >= 0:
                count += 1
                nums[i], i = -1, nums[i]
            if count > res:
                    res = count
        return res