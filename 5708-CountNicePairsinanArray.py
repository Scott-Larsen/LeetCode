# https://leetcode.com/contest/biweekly-contest-49/problems/count-nice-pairs-in-an-array/

# You are given an array nums that consists of non-negative integers. Let us define
# rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321,
# and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the
# following conditions:

#     0 <= i < j < nums.length
#     nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

# Return the number of nice pairs of indices. Since that number can be too large,
# return it modulo 109 + 7.


from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def reverse(number):
            if number not in reverses:
                reverses[number] = int(str(number)[::-1])
            return reverses[number]

        res = 0
        reverses = {}

        # Stores the number of nums that produce that answer with the answer as the key.
        answers = defaultdict(int)

        # Iterates backwards because j must be after i.
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in reverses:
                reverses[nums[i]] = reverse(nums[i])
            res += answers[nums[i] - reverse(nums[i])]
            answers[nums[i] - reverse(nums[i])] += 1
        return res % (10 ** 9 + 7)
