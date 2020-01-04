# https://leetcode.com/problems/check-if-it-is-a-straight-line/

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
# represents the coordinate of a point. Check if these points make a straight
# line in the XY plane.

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        try:
            ratio = float(coordinates[1][0] - coordinates[0][0]) / (coordinates[1][1] - coordinates[0][1])
        except:
            for j in range(1, len(coordinates)):
                if coordinates[0][1] != coordinates[j][1]:
                    return False
            return True
        for i in range(2, len(coordinates)):
            try:
                if ratio != float(coordinates[i][0] - coordinates[0][0]) / (coordinates[i][1] - coordinates[0][1]):
                    return False
            except:
                return False
        return True