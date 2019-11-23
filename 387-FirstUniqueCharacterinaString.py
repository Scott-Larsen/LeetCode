# https://leetcode.com/problems/first-unique-character-in-a-string/

#  Given a string, find the first non-repeating character in it and return it's
#  index. If it doesn't exist, return -1. 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1