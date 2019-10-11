# Given an array of distinct integers arr, find all pairs of elements with the
# minimum absolute difference of any two elements. 

# Return a list of pairs in ascending order(with respect to pairs), each pair
# [a, b] follows

#     a, b are from arr a < b b - a equals to the minimum absolute difference of
#     any two elements in arr


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = min([arr[x + 1] - arr[x] for x in range(len(arr) - 1)])
        return [[arr[x], arr[x + 1]] for x in range(len(arr) - 1) if arr[x + 1] - arr[x] == diff]