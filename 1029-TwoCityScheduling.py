# https://leetcode.com/problems/two-city-scheduling/

# There are 2N people a company is planning to interview. The cost of flying the
# i-th person to city A is costs[i][0], and the cost of flying the i-th person
# to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that exactly N
# people arrive in each city.

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda c: abs(c[0] - c[1]), reverse=True)
        l, r, half, price = 0, 0, len(costs) / 2, 0
        for cost in costs:
            if cost[0] < cost[1]:
                if l < half:
                    price += cost[0]
                    l += 1
                else:
                    price += cost[1]
                    r += 1
            else:
                if r < half:
                    price += cost[1]
                    r += 1
                else:
                    price += cost[0]
                    l += 1
        return price