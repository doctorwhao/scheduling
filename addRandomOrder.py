import random
def addorder(listOfTheDictionary):
    numbers = len(listOfTheDictionary)
    a = []
    for i in range(0,numbers):
        a.append(i)
    for j in listOfTheDictionary:
        status = True
        while status:
            randomNumber = random.randint(0, numbers - 1)
            if randomNumber in a:
                j["Order"] = randomNumber
                a.remove(randomNumber)
                status = False
            else:
                status = True
    return listOfTheDictionary







