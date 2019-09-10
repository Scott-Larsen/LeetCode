# Write a function that reverses a string. The input string is given as an array
# of characters char[].

# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s.reverse()
        
        # Don't understand why this doesn't work.
        # for i in range(0, len(s) - 1):
        #     char = s.pop(-1)
        #     s = s[:i] + [char] + s[i:]