d = {}


def putInDict(pair):
    if pair[0] not in d.keys():
        d[pair[0]] = [pair[1]]
    else:
        d[pair[0]].append(pair[1])


def pullFromDict(entry):
    if entry in d.keys():
        ret = d[entry].pop()
        if len(d[entry]) == 0:
            del d[entry]
        d[ret].remove(entry)
        if len(d[ret]) == 0:
            del d[ret]
        return ret
    return False


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) <= 1:
            return adjacentPairs[0]
        else:
            res = adjacentPairs.pop()
            start, end = res[0], res[1]
            revStart = []
            for pair in adjacentPairs:
                putInDict(pair)
                putInDict(pair[::-1])

            while d:
                newStart = pullFromDict(start)
                if newStart is not False:
                    revStart.append(newStart)
                    start = revStart[-1]
                newEnd = pullFromDict(end)
                if newEnd is not False:
                    res.append(newEnd)
                    end = res[-1]
            return revStart[::-1] + res