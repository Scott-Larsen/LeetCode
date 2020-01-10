# https://leetcode.com/problems/longest-word-in-dictionary/

# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other words
# in words. If there is more than one possible answer, return the longest word
# with the smallest lexicographical order. If there is no answer, return the
# empty string. 

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = len, reverse = True)
        while True:
            currentLength = []
            while len(currentLength) == 0 or words and len(words[0]) == len(currentLength[0]):
                currentLength.append(words.pop(0))
            currentLength.sort()
            if len(currentLength[0]) == 1:
                return currentLength[0]
            for j in range(len(currentLength)):
                word = currentLength[j]
                for i in range(len(word) - 1, 0, -1):
                    if word[:i] not in words:
                        break
                    elif i == 1:
                        return word
        return ""