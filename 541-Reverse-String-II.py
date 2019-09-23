#  Given a string and an integer k, you need to reverse the first k characters
#  for every 2k characters counting from the start of the string. If there are
#  less than k characters left, reverse all of them. If there are less than 2k
#  but greater than or equal to k characters, then reverse the first k
#  characters and left the other as original. 

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        newString = ""
        while len(s) > 0:
            newString += s[k - 1::-1] + s[k: 2 * k]
            s = s[2 * k:]
        return newString