# A conveyor belt has packages that must be shipped from one port to another
# within D days.

# The i-th package on the conveyor belt has a weight of weights[i].  Each day,
# we load the ship with packages on the conveyor belt (in the order given by
# weights). We may not load more weight than the maximum weight capacity of the
# ship.

# Return the least weight capacity of the ship that will result in all the
# packages on the conveyor belt being shipped within D days.

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lowestNotWorking, lowestWorking = max(weights) - 1, sum(weights)
        while lowestWorking - lowestNotWorking != 1:
            guess = (lowestWorking + lowestNotWorking) // 2
            runningTotal, ships = 0, 0
            for w in weights:
                if runningTotal + w < guess:
                    runningTotal += w
                elif runningTotal + w > guess:
                    runningTotal = w
                    ships += 1
                else:
                    runningTotal = 0
                    ships += 1
            if runningTotal:
                ships += 1
            if ships <= D:
                lowestWorking = guess
            else:
                lowestNotWorking = guess
        return lowestWorking