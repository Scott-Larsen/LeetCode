def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    else:
        l = []
        for i in range(len(nums)):
            x = nums[i]
            xs = nums[:i] + nums[i + 1 :]
            for j in permute(xs):
                l.append([x] + j)
        return l

# print(permute(list('abc')))
print(permute([1,2,3]))