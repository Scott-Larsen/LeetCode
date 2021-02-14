class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        elevation = 0
        maxElevation = 0
        for i in range(len(gain)):
            elevation += gain[i]
            if elevation > maxElevation:
                maxElevation = elevation
        return maxElevation