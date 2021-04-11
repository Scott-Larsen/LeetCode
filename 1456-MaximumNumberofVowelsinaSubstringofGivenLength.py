# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# Given a string s and an integer k.

# Return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are (a, e, i, o, u).

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max = 0
        current = 0
        start = 0
        end = 0
        while end < len(s):
            while (end - start) < k:
                if s[end] in "aeiou":
                    current += 1
                    if current > max:
                        max = current
                end += 1
            if s[start] in "aeiou":
                current -= 1
            start += 1
        return max