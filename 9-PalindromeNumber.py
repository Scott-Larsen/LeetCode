# https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        while len(x) > 1:
            if x[0] != x[-1]:
                return False
            x = x[1:-1]
        return True