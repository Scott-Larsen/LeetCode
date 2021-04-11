# https://leetcode.com/contest/weekly-contest-236/problems/sign-of-the-product-of-an-array

# There is a function signFunc(x) that returns:

#     1 if x is positive.
#     -1 if x is negative.
#     0 if x is equal to 0.

# You are given an integer array nums. Let product be the product of all values
# in the array nums.

# Return signFunc(product).


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        pos = True
        for num in nums:
            if num < 0:
                pos = False if pos == True else True
            elif num == 0:
                return 0
        if pos == True:
            return 1
        return -1