# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        else:
            x, y = 0, 1
            for i in range(2, N + 1):
                x, y = y, x + y
            return y

    # Recursive
        # if N <= 1:
        #     return N
        # else:
        #     return(self.fib(N-1) + self.fib(N-2))