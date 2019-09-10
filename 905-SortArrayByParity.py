# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odds = []
        for i in range(len(A) -1, -1, -1):
            if A[i] % 2 != 0:
                odds.append(A.pop(i))
        return A + odds