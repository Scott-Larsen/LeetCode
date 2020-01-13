# https://leetcode.com/problems/grumpy-bookstore-owner/

# Today, the bookstore owner has a store open for customers.length minutes.
# Every minute, some number of customers (customers[i]) enter the store, and all
# those customers leave after the end of that minute.

# On some minutes, the bookstore owner is grumpy.  If the bookstore owner is
# grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the
# bookstore owner is grumpy, the customers of that minute are not satisfied,
# otherwise they are satisfied.

# The bookstore owner knows a secret technique to keep themselves not grumpy for
# X minutes straight, but can only use it once.

# Return the maximum number of customers that can be satisfied throughout the
# day.

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = 0
        current = [customers[i] * (1 - grumpy[i]) for i in range(len(customers))]
        res = sum(customers[:X]) + sum(current[X:])
        current = res
        for j in range(len(customers) - X):
            if grumpy[j]:
                current -= customers[j]
            if grumpy[j + X]:
                    current += customers[j + X]
            if current > res:
                res = current
        return res