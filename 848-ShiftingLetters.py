# We have a string S of lowercase letters, and an integer array shifts.
# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.
# Return the final string after all such shifts to S are applied.

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        s = list(S)
        newShiftsSum = 0
        for i in range(len(S) - 1, -1, -1):
            newShiftsSum += shifts[i]
            s[i] = chr(((ord(s[i]) + newShiftsSum - 97) % 26) + 97)
        return "".join(s)

