# https://leetcode.com/contest/biweekly-contest-54/problems/check-if-all-the-integers-in-a-range-are-covered/

# You are given a 2D integer array ranges and two integers left and right. Each
# ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

# Return true if each integer in the inclusive range [left, right] is covered by at
# least one interval in ranges. Return false otherwise.

# An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <=
# endi.


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        d = {}
        for range_ in ranges:
            for i in range(range_[0], range_[1] + 1):
                d[i] = 1

        for j in range(left, right + 1):
            try:
                d[j]
            except:
                return False
        return True
