from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        aAlpha, bAlpha = [0] * 26, [0] * 26
        for letter in a:
            aAlpha[ord(letter) - 97] += 1
        for letter in b:
            bAlpha[ord(letter) - 97] += 1
        minChange = 99999999999
        for i in range(1, 26):
            greaterThan = min(
                sum(aAlpha[i:26]) + sum(bAlpha[:i]), sum(bAlpha[i:26]) + sum(aAlpha[:i])
            )
            lessThan = min(
                sum(aAlpha[:i]) + sum(bAlpha[i:26]), sum(bAlpha[:i]) + sum(aAlpha[i:26])
            )
            if min(greaterThan, lessThan) < minChange:
                minChange = min(greaterThan, lessThan)

        ca = Counter(a)
        cb = Counter(b)
        cab = ca + cb
        # print(cab)
        max = total = 0
        for letter in cab.keys():
            if cab[letter] > max:
                max = cab[letter]
            total += cab[letter]
        sameLetter = total - max
        return min(sameLetter, minChange)