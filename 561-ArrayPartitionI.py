#  Given an array of 2n integers, your task is to group these integers into n
#  pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of
#  min(ai, bi) for all i from 1 to n as large as possible. 

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        m = [min(nums[x], nums[x + 1]) for x in range(0, len(nums), 2)]
        return sum(m)