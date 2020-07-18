# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = defaultdict(int)
        for i in range(len(arr)):
            d[arr[i]] += 1
        keys = list(set(arr))
        keys = sorted(keys, key = lambda j : d[j])
        while k > 0:
            k, d[keys[0]] = k - d[keys[0]], d[keys[0]] - k
            if d[keys[0]] <= 0:
                keys.pop(0)
        return len(keys)