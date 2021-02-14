# 5677. Count Number of Homogenous Substrings

# Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

# A string is homogenous if all the characters of the string are the same.

# A substring is a contiguous sequence of characters within a string.


class Solution:
    def countHomogenous(self, s: str) -> int:
        currentLetter = None
        currentCount = 0
        res = 0
        f = {}

        def factorial(num, f):
            if num in f.keys():
                return f[num]
            else:
                if num == 0:
                    return 0
                elif num == 1:
                    return 1
                else:
                    res = num + factorial(num - 1, f)
                    f[num] = res
                    return res

        for i, v in enumerate(s):
            if v == currentLetter or currentLetter == None:
                currentCount += 1
            else:
                res += factorial(currentCount, f)
                currentCount = 1
            currentLetter = v

            if i == len(s) - 1:
                res += factorial(currentCount, f)
                return res % (10 ** 9 + 7)
