class Solution:
    def maximumTime(self, time: str) -> str:
        outputTime = []
        t = "23:59"
        for i in range(len(time)):
            if time[i] == "?":
                if i == 0:
                    if time[0:2] == "??":
                        outputTime.append("2")
                        i += 1
                    elif int(time[1]) > 3:
                        outputTime.append("1")
                    else:
                        outputTime.append("2")
                elif i == 1:
                    if outputTime[0] == "2" or time[0] == "2":
                        outputTime.append("3")
                    else:
                        outputTime.append("9")
                else:
                    outputTime.append(t[i])
            else:
                outputTime.append(time[i])
        return "".join(outputTime)
