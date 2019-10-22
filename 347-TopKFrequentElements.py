# Given a non-empty array of integers, return the k most frequent elements.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        return sorted(c, key = c.__getitem__, reverse = True)[0: k]