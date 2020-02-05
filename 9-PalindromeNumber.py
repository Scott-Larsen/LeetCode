# https://leetcode.com/problems/palindrome-number/

# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers = []
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            while x > 0:
                newX = int(x / 10)
                numbers.append(x - newX * 10)
                x = newX
            return True if numbers == numbers[::-1] else False
        return False            
        
        # Done with strings
        # x = str(x)
        # while len(x) > 1:
        #     if x[0] != x[-1]:
        #         return False
        #     x = x[1:-1]
        # return True