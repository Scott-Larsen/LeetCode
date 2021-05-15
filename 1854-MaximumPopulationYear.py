# https://leetcode.com/contest/weekly-contest-240/problems/maximum-population-year/

# You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates
# the birth and death years of the ith person.

# The population of some year x is the number of people alive during that year. The ith
# person is counted in year x's population if x is in the inclusive range
# [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

# Return the earliest year with the maximum population.


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        year = logs[0][0]
        max = 0
        pop = [0] * 100
        for log in logs:
            for i in range(log[0] - 1950, log[1] - 1950, 1):
                pop[i] += 1
                if pop[i] > max:
                    max = pop[i]
                    year = 1950 + i
        return year
