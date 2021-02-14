class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                newNums = nums[i + 1 :] + nums[: i + 1]
                for j in range(len(newNums) - 1):
                    if newNums[j] > newNums[j + 1]:
                        return False
                return True
        return True
