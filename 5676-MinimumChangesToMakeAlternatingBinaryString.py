# 5676. Minimum Changes To Make Alternating Binary String

# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.


class Solution:
    def minOperations(self, s: str) -> int:
        evenOne, oddOne = 0, 0
        alt = 0
        for i, v in enumerate(s):
            alt = str(i % 2)
            if v == alt:
                evenOne += 1
            else:
                oddOne += 1
        return min(evenOne, oddOne)
