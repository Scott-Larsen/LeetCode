# 5659. Minimum Length of String After Deleting Similar Ends

# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

#     Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
#     Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
#     The prefix and the suffix should not intersect at any index.
#     The characters from the prefix and suffix must be the same.
#     Delete both the prefix and the suffix.

# Return the minimum length of s after performing the above operation any number of times (possibly zero times).


class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        while s[0] == s[-1]:
            if len(s) <= 2:
                return len(s) % 2
            letter = s[0]
            while s[0] == letter:
                if len(s) == 1:
                    return 0
                s = s[1:]
            while s[-1] == letter:
                s = s[:-1]
        return len(s)
