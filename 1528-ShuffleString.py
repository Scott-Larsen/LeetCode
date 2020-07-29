# https://leetcode.com/problems/shuffle-string/

# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newString = []
        for i in range(len(indices)):
            newString.append(s[indices.index(i)])
        return "".join(newString)