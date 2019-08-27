# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of
# times.

from itertools import combinations_with_replacement
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        c = [combinations_with_replacement(candidates, i) for i in range(1, target // min(candidates) + 1)]
        newCombinations = []
        for j in range(len(c)):
            newCombinations.extend(list(c[j]))
            
        finalCombinations = []
        for k in range(len(newCombinations)):
            if sum(newCombinations[k]) == target:
                finalCombinations += [newCombinations[k]]
        
        return finalCombinations