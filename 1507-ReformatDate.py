# https://leetcode.com/problems/reformat-date/

# Given a date string in the form Day Month Year, where:

#     Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
#     Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
#     Year is in the range [1900, 2100].

# Convert the date string to the format YYYY-MM-DD, where:

#     YYYY denotes the 4 digit year.
#     MM denotes the 2 digit month.
#     DD denotes the 2 digit day.

class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date = date.split()
        def make_two_digit(x):
            return str(0) + x if len(x) < 2 else x
        return date[2] + "-" + make_two_digit(str(months.index(date[1]) + 1))  + "-" + make_two_digit(date[0][:-2])