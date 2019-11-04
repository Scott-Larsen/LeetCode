# Given an array A of integers, return true if and only if we can partition the
# array into three non-empty parts with equal sums.

# Formally, we can partition the array if we can find indexes i+1 < j with (A[0]
# + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... +
# A[A.length - 1])

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = (sum(A)) / 3
        if s == int(s):
            i, runningSum, count = 0, 0, 0
            while i < len(A):
                runningSum += A[i]
                if runningSum == s:
                    count += 1
                    runningSum = 0
                i += 1
            if count == 3:
                return True
            return False