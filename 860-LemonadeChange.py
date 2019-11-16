# https://leetcode.com/problems/lemonade-change/

# At a lemonade stand, each lemonade costs $5. 

# Customers are standing in a queue to buy from you, and order one at a time (in
# the order specified by bills).

# Each customer will only buy one lemonade and pay with either a $5, $10, or $20
# bill.  You must provide the correct change to each customer, so that the net
# transaction is that the customer pays $5.

# Note that you don't have any change in hand at first.

# Return true if and only if you can provide every customer with correct change.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = collections.defaultdict(int)
        for bill in bills:
            if bill == 5:
                notes[5] += 1
            elif bill == 10:
                if notes[5] >= 1:
                    notes[5] -= 1
                    notes[10] += 1
                else:
                    return False
            else:
                if notes[5] >= 1 and notes[10] >= 1:
                    notes[5] -= 1
                    notes[10] -= 1
                elif notes[5] >= 3:
                    notes[5] -= 3
                else:
                    return False
        return True