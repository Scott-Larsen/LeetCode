# In a array A of size 2N, there are N+1 unique elements, and exactly one of
# these elements is repeated N times.

# Return the element repeated N times.

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        repeats = collections.defaultdict(int)
        for num in A:
            repeats[num] += 1
        for key in repeats.keys():
            if repeats[key] == len(A) / 2:
                return key