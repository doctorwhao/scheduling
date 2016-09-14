f = open("fromExcel","r")
lines = f.readlines()
readMessageFromTxt = []
for line in lines:
    line = line.strip("\n")
    readMessageFromTxt.append(line)
numberOfPeople = len(readMessageFromTxt)
f.close()
listOfDictionary = []
for i in readMessageFromTxt:
    middleDict = dict()
    splitObject = i.split('.')
    middleDict["Name"] = splitObject[0]
    k = splitObject[1].strip("(")
    l = k.strip(")")
    m = l.split(",")
    middleDict["EmptyTime"] = m
    middleDict["TimesOfPerWeek"] = splitObject[2]
    middleDict["Order"] = 0
    listOfDictionary.append(middleDict)
print(listOfDictionary)



