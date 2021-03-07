# 5682. Sum of Beauty of All Substrings

# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

#     For example, the beauty of "abaacc" is 3 - 1 = 2.

# Given a string s, return the sum of beauty of all of its substrings.

from collections import defaultdict


def checkBeauty(dict_):
    vals = [v for k, v in dict_.items()]
    min_, max_ = min(vals), max(vals)
    return max_ - min_


class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(3, len(s) + 1):
            d = defaultdict(int)
            for char in s[:i]:
                d[char] += 1
            res += checkBeauty(d)
            for j in range(i, len(s)):
                d[s[j]] += 1
                if d[s[j - i]] > 1:
                    d[s[j - i]] -= 1
                else:
                    del d[s[j - i]]
                res += checkBeauty(d)
        return res
