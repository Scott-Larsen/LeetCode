# You are given a string s that consists of lower case English letters and
# brackets. 

# Reverse the strings in each pair of matching parentheses, starting from the
# innermost one.

# Your result should not contain any brackets.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        while ")" in s:
            i = s.index(")")
            j = i - 1
            while j >= 0:
                if s[j] == "(":
                    s = s[:j] + s[i - 1:j:-1] + s[i + 1:]
                    break
                j -= 1
        return s