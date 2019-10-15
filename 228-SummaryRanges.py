# Given a sorted integer array without duplicates, return the summary of its
# ranges.

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        first, r = None, []
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                if first == None:
                    first = nums[i]
                if i == len(nums) - 2:# and first < nums[i]:
                    r.append(f"{first}->{nums[-1]}")
            elif first != None:
                r.append(f"{first}->{nums[i]}")
                first = None
            else:
                r.append(f"{nums[i]}")
                first = None
        if len(nums) == 1 or len(nums) > 1 and nums[-1] - nums[-2] > 1:
            r.append(f"{nums[-1]}")
        return r