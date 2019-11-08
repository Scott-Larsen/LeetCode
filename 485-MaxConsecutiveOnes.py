# Given a binary array, find the maximum number of consecutive 1s in this array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:    
        n = str(nums)
        n = [char for char in n if char == "1" or char == "0"]
        n = "".join(n)
        n = n.split("0")
        return max([len(i) for i in n])