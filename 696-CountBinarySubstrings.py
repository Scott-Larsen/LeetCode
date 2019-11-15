# https://leetcode.com/problems/count-binary-substrings/

# Give a string s, count the number of non-empty (contiguous) substrings that
# have the same number of 0's and 1's, and all the 0's and all the 1's in these
# substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they
# occur.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        for i in range(1, len(s)):
            offset = 1
            while i - offset >= 0 and i + offset - 1 < len(s) and s[i - offset] != s[i + offset - 1]:
                if offset > 1 and s[i - offset] == s[i - offset + 1]:
                    count += 1
                elif offset == 1:                        
                    count += 1
                else:
                    break
                offset += 1
        return count