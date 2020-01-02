# https://leetcode.com/problems/happy-number/

# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any
# positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1. Those numbers for which
# this process ends in 1 are happy numbers.

class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(20):
            n = str(n)
            s = 0
            for char in n:
                s += int(char)**2
            if s == 1:
                return "true"
            else:
                n = s
        return False