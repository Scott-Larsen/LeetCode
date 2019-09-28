# In a string S of lowercase letters, these letters form consecutive groups of
# the same character.

# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx",
# "z" and "yy".

# Call a group large if it has 3 or more characters.  We would like the starting
# and ending positions of every large group.

# The final answer should be in lexicographic order.

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        LGP = []
        if len(S) >= 3:
            newS = S[0]
            for i in range(1, len(S)):
                if S[i] == S[i-1]:
                    newS += S[i]
                else:
                    newS += f",{S[i]}"
            SList = newS.split(",")
            # print(SList)
            start = 0
            for j in range(len(SList)):
                if len(SList[j]) >= 3:
                    LGP.append([start, start + len(SList[j]) - 1])
                start += len(SList[j])
        return LGP