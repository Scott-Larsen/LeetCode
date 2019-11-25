# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

# Given an array A of integers, we must modify the array in the following way:
# we choose an i and replace A[i] with -A[i], and we repeat this process K times
# in total.  (We may choose the same index i multiple times.)

# Return the largest possible sum of the array after modifying it in this way.

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i in range(len(A)):
            if K == 0:
                return sum(A)
            elif A[i] != abs(A[i]):
                A[i] = -A[i]
                K -= 1
            else:
                if K % 2 == 0:
                    return sum(A)
                else:
                    return sum(A) - 2 * min(A)