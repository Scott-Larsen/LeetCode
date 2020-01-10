# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] =
# [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is,
# one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and
# dominoes[i] is equivalent to dominoes[j].

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        d = collections.defaultdict(int)
        for domino in dominoes:
            if domino[0] <= domino[1]:
                d[tuple(domino)] += 1
            else:
                reverse = [domino[1], domino[0]]
                d[tuple(reverse)] += 1
        for k in d.keys():
            if d[k] > 1:
                k = d[k] - 1
                while k > 0:
                    res += k
                    k -= 1
        return res