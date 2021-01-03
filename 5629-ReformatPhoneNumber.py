class Solution:
    def reformatNumber(self, number: str) -> str:
        res = []
        numList = []
        groupings = []
        for char in number:
            if char in "- ":
                pass
            else:
                numList.append(char)
        while len(numList) > 4:
            groupings.append("".join(numList[:3]))
            numList = numList[3:]
        if len(numList) == 4:
            groupings.append("".join(numList[:2]))
            numList = numList[2:]
        groupings.append("".join(numList))
        return "-".join(groupings)            