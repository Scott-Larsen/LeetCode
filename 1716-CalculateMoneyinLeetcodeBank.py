class Solution:
    def totalMoney(self, n: int) -> int:
        baseWeek = 28
        res = 0
        fullWeeks, remainingDays = divmod(n, 7)
        res += baseWeek * fullWeeks
        weeklyBonus, numberOfWeeks = 0, fullWeeks
        while fullWeeks:
            res += weeklyBonus
            weeklyBonus += 7
            fullWeeks -= 1
        compoundedDaily = numberOfWeeks + 1
        while remainingDays:
            res += compoundedDaily
            compoundedDaily += 1
            remainingDays -= 1
        return res