# https://leetcode.com/contest/weekly-contest-236/problems/finding-mk-average/

# You are given two integers, m and k, and a stream of integers. You are tasked
# to implement a data structure that calculates the MKAverage for the stream.

# The MKAverage can be calculated using these steps:

#     If the number of the elements in the stream is less than m you should
# consider the MKAverage to be -1. Otherwise, copy the last m elements of the
# stream to a separate container.
#     Remove the smallest k elements and the largest k elements from the
# container.
#     Calculate the average value for the rest of the elements rounded down to
# the nearest integer.

# Implement the MKAverage class:

#     MKAverage(int m, int k) Initializes the MKAverage object with an empty
# stream and the two integers m and k.
#     void addElement(int num) Inserts a new element num into the stream.
#     int calculateMKAverage() Calculates and returns the MKAverage for the
# current stream rounded down to the nearest integer.


class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.list_ = []

    def addElement(self, num: int) -> None:
        self.list_.append(num)

    def calculateMKAverage(self) -> int:
        if len(self.list_) < self.m:
            return -1
        else:
            self.copied_list = self.list_[-self.m :]
            self.copied_list.sort()
            self.shortened_list = self.copied_list[self.k : -self.k]
            return int(sum(self.shortened_list) / len(self.shortened_list))


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()