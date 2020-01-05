# https://leetcode.com/problems/backspace-string-compare/

# Given two strings S and T, return if they are equal when both are typed into
# empty text editors. # means a backspace character.

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def evaluateString(s):
            returnString = ""
            for char in s:
                if char == "#":
                    if len(returnString) >= 1:
                        returnString = returnString[:-1]
                else:
                    returnString += char
            return returnString
        if evaluateString(S) == evaluateString(T):
            return True
        return False