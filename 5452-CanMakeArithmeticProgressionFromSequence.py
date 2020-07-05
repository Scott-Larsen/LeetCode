# https://leetcode.com/contest/weekly-contest-196/problems/can-make-arithmetic-progression-from-sequence/

# Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

# Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        spacing = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != spacing:
                return False
        return True