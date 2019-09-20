def combinationSum2(candidates, target):
    if len(candidates) == 0:
        return []
    elif len(candidates) == 1:
        return [candidates]
    else:
        combos = []
        for i in range(len(candidates)):
            x = candidates[i]
            y = candidates[:i] + candidates[i + 1:]
            for j in combinationSum2(y, target):
                # if sum([x] + j) == target:
                # print(f"combos = {combos}")
                # print([x] + j)
                if ([x] + j) not in combos:
                    combos.append(([x] + j))
                if j not in combos:
                    combos.append(j)
        # return combos

    print(combos)

    # equalSum = []
    # for l in combos:
    #     # print(l)
    #     if sum(l) == target:
    #         print(l)
    #         equalSum.append(l)

    # return equalSum

c = combinationSum2([10,1,2,7,6,1,5], 8)
# c = combinationSum2([10,1,2,7,6,1,5], 8)
# print((combinationSum2([10,1,2], 8)))

# print(len(c))
# print(c)
# print(len(equalSum))
# print(equalSum)
