# You are driving a vehicle that has capacity empty seats initially available
# for passengers.  The vehicle only drives east (ie. it cannot turn around and
# drive west.)

# Given a list of trips, trip[i] = [num_passengers, start_location,
# end_location] contains information about the i-th trip: the number of
# passengers that must be picked up, and the locations to pick them up and drop
# them off.  The locations are given as the number of kilometers due east from
# your vehicle's initial location.

# Return true if and only if it is possible to pick up and drop off all
# passengers for all the given trips. 

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = collections.defaultdict(int)
        for trip in trips:
            for stop in range(trip[1], trip[2]):
                car[stop] += trip[0]
        for key in car.keys():
            if car[key] > capacity:
                return False
        return True