# https://leetcode.com/contest/biweekly-contest-51/problems/replace-all-digits-with-characters/

# You are given a 0-indexed string s that has lowercase English letters in its even
# indices and digits in its odd indices.

# There is a function shift(c, x), where c is a character and x is a digit, that
# returns the xth character after c.

#     For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.

# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will
# never exceed 'z'.


class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        for i in range(0, len(s), 2):
            res.append(s[i])
            if i + 1 < len(s):
                res.append(chr(ord(s[i]) + int(s[i + 1])))
        return "".join(res)
