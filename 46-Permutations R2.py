def permute(nums):
	if len(nums) == 0:
		yield []
	elif len(nums) == 1:
		yield nums
	else:
		l = []
		for i in range(len(nums)):
			x = nums[i]
			xs = nums[:i] + nums[i + 1:]
			for j in permute(xs):
				yield ([x] + j)

print(list(permute([1,2,3])))