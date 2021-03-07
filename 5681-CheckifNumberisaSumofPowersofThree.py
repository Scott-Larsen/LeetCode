# 5681. Check if Number is a Sum of Powers of Three

# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3x.


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        t, threes = 1, [1]
        while t <= n:
            t *= 3
            if t <= n:
                threes.append(t)

        sums = [0]
        while threes:
            three = threes.pop(0)
            for i in range(len(sums) - 1, -1, -1):
                newSum = three + sums[i]
                if newSum == n:
                    return True
                else:
                    sums.append(newSum)
        return False

