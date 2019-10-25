# Given an array A of non-negative integers, return the maximum sum of elements
# in two non-overlapping (contiguous) subarrays, which have lengths L and M.
# (For clarification, the L-length subarray could occur before or after the
# M-length subarray.)

# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1])
# + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        maximum, minimum, res = max([L, M]), min(L, M), 0
        for i in range(len(A) - maximum + 1):
            firstMax = sum(A[i: i + maximum])
            secondMax = 0
            before, after = A[:i], A[i + maximum:]
            if len(before) >= minimum:
                for j in range(len(before) - minimum):
                    if sum(before[j: j + minimum]) > secondMax:
                        secondMax = sum(before[j: j + minimum])
            if len(after) >= minimum:
                for k in range(len(after) - minimum + 1):
                    if sum(after[k: k + minimum]) > secondMax:
                        secondMax = sum(after[k: k + minimum])
            if firstMax + secondMax > res:
                res = firstMax + secondMax
        return res