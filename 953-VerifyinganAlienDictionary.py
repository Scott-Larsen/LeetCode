# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order. The order of the alphabet is some
# permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted
# lexicographicaly in this alien language.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) > 1:
            for i in range(len(words) - 1):
                j = 0
                k = min(len(words[i]), len(words[i + 1]))
                while words[i][j] == words[i + 1][j] and j < k:
                    if i == j - 1:
                        if len(words[i]) > len(words[i + 1]):
                            return False
                    j += 1

                if order.index(words[i][j]) > order.index(words[i + 1][j]):
                    return False
        return True