# We are given two arrays A and B of words.  Each word is a string of lowercase
# letters.

# Now, say that word b is a subset of word a if every letter in b occurs in a,
# including multiplicity.  For example, "wrr" is a subset of "warrior", but is
# not a subset of "world".

# Now say a word a from A is universal if for every b in B, b is a subset of a. 

# Return a list of all universal words in A.  You can return the words in any
# order.

# from collections import Counter, defaultdict

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        words = A[:]
        B = list(set(B))
        B.sort(key = len, reverse = True)
        metaB = defaultdict(int)
        for b in B:
            bCounter = Counter(b)
            for char in bCounter:
                metaB[char] = max(metaB[char], bCounter[char])
        for a in A:
            aCounter = Counter(a)
            for letter in metaB:
                if metaB[letter] > aCounter[letter]:
                    words.remove(a)
                    break
        return words