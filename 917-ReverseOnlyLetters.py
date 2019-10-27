# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their positions.

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        r = S[::-1]
        for i in range(len(r) - 1, -1, -1):
            if not r[i].isalpha():
                r = r[:i] + r[i + 1:]
        for j in range(len(S)):
            if not S[j].isalpha():
                r = r[:j] + S[j] + r[j:]
        return r