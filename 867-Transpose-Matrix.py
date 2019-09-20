# Given a matrix A, return the transpose of A.

# The transpose of a matrix is the matrix flipped over it's main diagonal,
# switching the row and column indices of the matrix.

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        transposedLists = []
        for i in range(len(A[0])):
            tList = []
            for j in range(len(A)):
                tList.append(A[j].pop())
                # tList += [tL]
            transposedLists.append(tList)
        transposedLists.reverse()
        return transposedLists