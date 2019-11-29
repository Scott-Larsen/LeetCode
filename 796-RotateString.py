# https://leetcode.com/problems/rotate-string/

# We are given two strings, A and B.

# A shift on A consists of taking string A and moving the leftmost character to
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
# after one shift on A. Return True if and only if A can become B after some
# number of shifts on A.

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        for i in range(1, len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False