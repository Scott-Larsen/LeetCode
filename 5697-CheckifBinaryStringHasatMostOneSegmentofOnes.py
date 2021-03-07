# 5697. Check if Binary String Has at Most One Segment of Ones

# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s = s.split("0")
        s.pop(0)
        for _, v in enumerate(s):
            if "1" in v:
                return False
        return True
