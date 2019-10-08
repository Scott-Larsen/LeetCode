# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character
# can only be used once).

# Return the sum of lengths of all good strings in words.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = 0
        charset = set((char for char in chars))
        for word in words:
            include = True
            for char in word:
                if chars.count(char) < word.count(char):
                    include = False
                    break
            if include == True:
                c += len(word)
        return c