# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        m = [[0, None]]
        for c in count:
            if count[c] == m[0][0]:
                m.append([count[c], c])
            elif count[c] > m[0][0]:
                m = [[count[c], c]]
        return min([len(nums[nums.index(m[i][1]):len(nums) - nums[::-1].index(m[i][1])]) for i in range(len(m))])