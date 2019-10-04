# We define a harmounious array as an array where the difference between its
# maximum value and its minimum value is exactly 1.

# Now, given an integer array, you need to find the length of its longest
# harmonious subsequence among all its possible subsequences.

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
        if len(d) <= 1:
            return 0
        total = 0
        k = set(nums)
        for x in k:
            if d[x] + d[x + 1] > total:
                if d[x] != 0 and d[x + 1] != 0:
                    total = d[x] + d[x + 1]
        return total