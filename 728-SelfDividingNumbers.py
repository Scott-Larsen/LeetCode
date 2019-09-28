#  A self-dividing number is a number that is divisible by every digit it
#  contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
# and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self
# dividing number, including the bounds if possible. 

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(left, right + 1):
            if "0" in str(i):
                continue
            else:
                num = str(i)
                # add = 
                for j in range(len(num)):
                    if i % int(num[j]) != 0:
                        break
                    elif j == len(num) - 1:
                        nums.append(i)
        return nums