# Given an array of integers arr, write a function that returns true if and only
# if the number of occurrences of each value in the array is unique.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = collections.defaultdict(int)
        for x in arr:
            d[x] += 1
        occurrences = []
        for key in d.keys():
            if d[key] not in occurrences:
                occurrences.append(d[key])
            else:
                return False
        return True