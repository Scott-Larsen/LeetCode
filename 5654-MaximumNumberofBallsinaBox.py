from collections import defaultdict


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)
        for i in range(lowLimit, highLimit + 1):
            currentBucket = 0
            while i:
                i, cb = divmod(i, 10)
                currentBucket += cb
            d[currentBucket] += 1
        return max([d[x] for x in d.keys()])