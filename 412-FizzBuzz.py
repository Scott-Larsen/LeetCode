# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”. For numbers which are multiples of
# both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for i in range(1, n + 1):
            if i % 3 == 0:
                if i % 5 == 0:
                    r.append("FizzBuzz")
                else:
                    r.append("Fizz")
            elif i % 5 == 0:
                r.append("Buzz")
            else:
                r.append(str(i))
        return r