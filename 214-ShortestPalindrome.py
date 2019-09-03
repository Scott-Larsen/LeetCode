# Given a string s, you are allowed to convert it to a palindrome by adding
# characters in front of it. Find and return the shortest palindrome you can
# find by performing this transformation.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        while s[:int(len(s) / 2)] != s[-1:-(int(len(s) / 2)) - 1: -1]:
            s = s[:i] + s[-i - 1] + s[i:]
            i += 1
        return s