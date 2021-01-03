class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        while truckSize and boxTypes:
            if boxTypes[0][0] == 0:
                boxTypes.pop(0)
            else:
                res += boxTypes[0][1]
                truckSize -= 1
                boxTypes[0][0] -= 1
        return res
