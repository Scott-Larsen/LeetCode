# https://leetcode.com/contest/weekly-contest-186/problems/maximum-score-after-splitting-a-string/

# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

class Solution:
    def maxScore(self, s: str) -> int:
        left = 0 if int(s[0]) == 1 else 1
        right = s[1:]
        rightSum = sum([int(y) for y in list(right)])
        max = left + rightSum
        while len(right) > 1:
            x = int(right[0])
            right = right[1:]
            if x == 0:
                left += 1
            else:
                rightSum -= 1
            if left + rightSum > max:
                max = left + rightSum
        return max