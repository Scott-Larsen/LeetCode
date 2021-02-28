# 5690. Closest Dessert Cost

# You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors and m types of toppings to choose from. You must follow these rules when making your dessert:

#     There must be exactly one ice cream base.
#     You can add one or more types of topping or have no toppings at all.
#     There are at most two of each type of topping.

# You are given three inputs:

#     baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
#     toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
#     target, an integer representing your target price for dessert.

# You want to make a dessert with a total cost as close to target as possible.

# Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.


class Solution:
    def closestCost(
        self, baseCosts: List[int], toppingCosts: List[int], target: int
    ) -> int:
        combos = set(baseCosts)
        for topping in toppingCosts:
            cmbs = list(combos)
            for c in cmbs:
                combos.add(topping + c)
                combos.add(2 * topping + c)
        if target in combos:
            return target
        i = 1
        while i <= target:
            if target - i in combos:
                return target - i
            elif target + i in combos:
                return target + i
            i += 1
        return min(baseCosts)