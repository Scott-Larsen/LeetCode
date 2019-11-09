# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.  Each digit must be rotated -
# we cannot choose to leave it alone.

# A number is valid if each digit remains a digit after rotation. 0, 1, and 8
# rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each
# other, and the rest of the numbers do not rotate to any other number and
# become invalid.

# Now given a positive number N, how many numbers X from 1 to N are good?

class Solution:
    def rotatedDigits(self, N: int) -> int:
        res = 0
        for i in range(1, N + 1):
            add = False
            for char in str(i):
                if char in '347':
                    add = False
                    break
                elif char in '2569':
                    add = True
            if add == True:
                res += 1
        return res