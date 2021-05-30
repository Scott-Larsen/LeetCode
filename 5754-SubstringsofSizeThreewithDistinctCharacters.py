# https://leetcode.com/contest/biweekly-contest-53/problems/substrings-of-size-three-with-distinct-characters/

# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every occurrence
# should be counted.

# A substring is a contiguous sequence of characters in a string.

from collections import Counter


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        currentString = s[:3]
        c = Counter(currentString)
        if len(c) == 3:
            res += 1
        c = dict(c)
        for i, v in enumerate(s[3:]):
            if v in c:
                c[v] += 1
            else:
                c[v] = 1
            if c[s[i]] > 1:
                c[s[i]] -= 1
            else:
                del c[s[i]]
            if len(c) == 3:
                res += 1
        return res
