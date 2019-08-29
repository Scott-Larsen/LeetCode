# Given a collection of distinct integers, return all possible permutations.

# This is what I'd actually do

# from itertools import permutations
# class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
        # return (permutations(nums, len(nums)))


# This is an exercise in recursion

def permute(nums):

	if len(nums) == 0:
		yield []
	elif len(nums) == 1:
		yield nums
	else:
		for i in range(len(nums)):
			x = nums[i]
			xs = nums[:i] + nums[i+1:]
			for p in permute(xs):
				yield [x] + p

data = list([1,2,3])
print('permute')
for p in permute(data):
	print(p)


