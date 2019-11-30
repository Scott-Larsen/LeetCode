# https://leetcode.com/problems/relative-ranks/

# Given scores of N athletes, find their relative ranks and the people with the
# top three highest scores, who will be awarded medals: "Gold Medal", "Silver
# Medal" and "Bronze Medal".

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        n = sorted(nums, reverse = True)
        medals = ["Gold Medal","Silver Medal","Bronze Medal"]
        for i in range(len(n)):
            if i < 3:
                nums[nums.index(n[i])] = medals[i]
            else:
                nums[nums.index(n[i])] = f"{i+1}"
        return nums