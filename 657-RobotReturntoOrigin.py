# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given
# a sequence of its moves, judge if this robot ends up at (0, 0) after it
# completes its moves.

# The move sequence is represented by a string, and the character moves[i]
# represents its ith move. Valid moves are R (right), L (left), U (up), and D
# (down). If the robot returns to the origin after it finishes all of its moves,
# return true. Otherwise, return false.

# Note: The way that the robot is "facing" is irrelevant. "R" will always make
# the robot move to the right once, "L" will always make it move left, etc.
# Also, assume that the magnitude of the robot's movement is the same for each
# move.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = collections.Counter(moves)
        if c['U'] == c['D'] and c['L'] == c['R']:
            return True
        return False
    
        # FIRST SOLUTION
        # result = [0, 0]
        # directions = {"L": ["x", -1], "R": ["x", 1], "U": ["y", 1], "D": ["y", -1]}
        # for char in moves:
        #     if directions[char][0] == "x":
        #         result[0] += directions[char][1]
        #     else:
        #         result[1] += directions[char][1]
        # if result[0] == 0 and result[1] == 0:
        #     return True
        # return False