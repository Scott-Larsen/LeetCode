# 1768. Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        res.extend(word1[i + 1 :])
        res.extend(word2[i + 1 :])
        return "".join(res)