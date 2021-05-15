# https://leetcode.com/contest/biweekly-contest-52/problems/incremental-memory-leak/

# You are given two integers memory1 and memory2 representing the available memory in
# bits on two memory sticks. There is currently a faulty program running that consumes
# an increasing amount of memory every second.

# At the ith second (starting from 1), i bits of memory are allocated to the stick with
# more available memory (or from the first memory stick if both have the same available
# memory). If neither stick has at least i bits of available memory, the program
# crashes.

# Return an array containing [crashTime, memory1crash, memory2crash], where crashTime
# is the time (in seconds) when the program crashed and memory1crash and memory2crash
# are the available bits of memory in the first and second sticks respectively.


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        time = 1
        while time <= memory1 or time <= memory2:
            if memory2 > memory1:
                memory2 -= time
            else:
                memory1 -= time
            time += 1
        return [time, memory1, memory2]
