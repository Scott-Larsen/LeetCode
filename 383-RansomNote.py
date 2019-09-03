# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return false.
# # Each letter in the magazine string can only be used once in your ransom note. 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for char in ransomNote:
            try:
                magazine.remove(char)
            except:
                return False
        return True