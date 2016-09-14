f = open("timetable","r")
lines = f.readlines()
readTimeTableFromText = []
listOfTimetableDict = []
dictOfTimetable = {}
for line in lines:
    line = line.strip("\n")
    readTimeTableFromText.append(line)
for i in readTimeTableFromText:
    j = i.split(",")
    k = dict()
    k["Time"] = j[0]
    k["Left"] = int(j[1])
    listOfTimetableDict.append(k)
    dictOfTimetable[j[0]] = int(j[1])



