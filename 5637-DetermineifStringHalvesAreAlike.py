class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = s.lower()
        l = len(s)
        first, second = s[:l//2], s[l//2:]
        def countVowels(wordHalf):
            res = 0
            for char in wordHalf:
                if char in vowels:
                    res += 1
            return res
        first, second = countVowels(first), countVowels(second)
        if first == second:
            return True
        return False