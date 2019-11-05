# Given a word, you need to judge whether the usage of capitals in it is right
# or not.

# We define the usage of capitals in a word to be right when one of the
# following cases holds:

#     All letters in this word are capitals, like "USA". All letters in this
#     word are not capitals, like "leetcode". Only the first letter in this word
#     is capital, like "Google".

# Otherwise, we define that this word doesn't use capitals in a right way. 

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower() or word[0] == word[0].upper() and word[1:] == word[1:].lower():
            return True
        return False