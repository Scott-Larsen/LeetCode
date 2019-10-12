# Given a string text, you want to use the characters of text to form as many
# instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of
# instances that can be formed.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count(char)//'balloon'.count(char) for char in set('balloon'))
    
        # t = list(text)
        # b = 0
        # while t:
        #     for char in 'balloon':
        #         if char in t:
        #             t.remove(char)
        #         else:
        #             return b
        #     b += 1
        # return b