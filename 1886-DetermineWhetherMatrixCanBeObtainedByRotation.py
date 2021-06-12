# https://leetcode.com/contest/weekly-contest-244/problems/determine-whether-matrix-can-be-obtained-by-rotation/

# Given two n x n binary matrices mat and target, return true if it is possible to make
# mat equal to target by rotating mat in 90-degree increments, or false otherwise.


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        rot180 = [i[::-1] for i in mat[::-1]]
        if rot180 == target:
            return True
        rot90, rot_neg90 = [], []
        for j in range(len(mat[0])):
            current_rot90 = []
            for k in range(len(mat)):
                current_rot90.append(mat[k][j])
            rot90.append(current_rot90)
            rot_neg90.append(current_rot90[::-1])
        if rot90[::-1] == target or rot_neg90 == target:
            return True
