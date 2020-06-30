# https://leetcode.com/problems/the-kth-factor-of-n/

# Given two positive integers n and k.

# A factor of an integer n is defined as an integer i where n % i == 0.

# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        if k == 1:
            return 1
        for i in range(2, n + 1):
            if n % i == 0:
                factors.append(i)
            if len(factors) == k:
                return factors[-1]
        return -1