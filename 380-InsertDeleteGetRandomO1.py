# 380. Insert Delete GetRandom O(1)

# Implement the RandomizedSet class:

#     bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
#     bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
#     int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

# Follow up: Could you implement the functions of the class with each function works in average O(1) time?

from random import choice


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.value:
            return False
        else:
            self.value[val] = 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.value:
            del self.value[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(list(self.value.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
