def determineOrder(Name,Timetable):
    selectedPiece = {}
    determined = {}
    newName1 = []
    for i in range(0,len(Name)):
        for j in Name:
            if j["Order"] == i:
                selectedPiece = j
        if selectedPiece["TimesOfPerWeek"] == 0:
            pass
        elif selectedPiece["TimesOfPerWeek"] == 1:
            for k in selectedPiece["EmptyTime"]:
                if Timetable[k] > 0:
                    Timetable[k] -= 1
                    if k in determined:
                        determined[k] = determined[k] + selectedPiece["Name"]
                    else:
                        determined[k] = selectedPiece["Name"] + " "
        elif selectedPiece["TimesOfPerWeek"] == 2:
            for k in selectedPiece["EmptyTime"]:
                if Timetable[k] > 0:
                    Timetable[k] -= 1
                    if k in determined:
                        determined[k] = determined[k] + selectedPiece["Name"]
                        aa = selectedPiece["EmptyTime"]
                        aa.remove(k)
                        selectedPiece["EmptyTime"] = aa
                        selectedPiece["TimesOfPerWeek"] -= 1
                        newName1.append(selectedPiece)
                    else:
                        determined[k] = selectedPiece["Name"] + " "
                        aa = selectedPiece["EmptyTime"]
                        aa.remove(k)
                        selectedPiece["EmptyTime"] = aa
                        selectedPiece["TimesOfPerWeek"] -= 1
                        newName1.append(selectedPiece)
    for i in range(0,len(newName1)):
        for j in newName1:
            if j["Order"] == i:
                selectedPiece = j
        if selectedPiece["TimesOfPerWeek"] == 0:
            pass
        elif selectedPiece["TimesOfPerWeek"] == 1:
            for k in selectedPiece["EmptyTime"]:
                if Timetable[k] > 0:
                    Timetable[k] -= 1
                    if k in determined:
                        determined[k] = determined[k] + selectedPiece["Name"]
                    else:
                        determined[k] = selectedPiece["Name"] + " "
    return determined




