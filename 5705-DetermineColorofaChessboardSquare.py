# 5705. Determine Color of a Chessboard Square

# You are given coordinates, a string that represents the coordinates of a
# square of the chessboard. Below is a chessboard for your reference.


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[0]) + int(coordinates[1])) % 2