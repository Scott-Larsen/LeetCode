# You are given two strings word1 and word2. You want to construct a string merge in the following way: while either word1 or word2 are non-empty, choose one of the following options:

#     If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
#         For example, if word1 = "abc" and merge = "dv", then after choosing this operation, word1 = "bc" and merge = "dva".
#     If word2 is non-empty, append the first character in word2 to merge and delete it from word2.
#         For example, if word2 = "abc" and merge = "", then after choosing this operation, word2 = "bc" and merge = "a".

# Return the lexicographically largest merge you can construct.

# A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b. For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = []
        word1 = list(word1)
        word2 = list(word2)

        def breakTie(w1, w2):
            l = min(len(w1), len(w2))
            for j in range(1, l):
                if w1[j] > w2[j]:
                    return 1
                elif w1[j] < w2[j]:
                    return 2
            if len(w1) > l:
                if w1[l] >= w1[l - 1]:
                    return 1
                else:
                    return 2
            elif len(w2) > l:
                if w2[l] >= w2[l - 1]:
                    return 2
                return 1
            return 1

        while word1 or word2:
            if len(word2) == 0:
                res.extend(word1)
                word1 = None
            elif len(word1) == 0:
                res.extend(word2)
                word2 = None
            else:
                if word1[0] > word2[0]:
                    res.extend(word1.pop(0))
                elif word1[0] < word2[0]:
                    res.extend(word2.pop(0))
                else:
                    if breakTie(word1, word2) == 1:
                        res.extend(word1.pop(0))
                    else:
                        res.extend(word2.pop(0))

        return "".join(res)
