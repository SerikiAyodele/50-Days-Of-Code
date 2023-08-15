# occurence of a string within a string

def occurence(givenString: str):
    maxCount = 0
    count = 1

    for i in range(1, len(givenString)):
        if givenString[i] == givenString[i - 1]:
            count = +1
        else:
            count = 1
        maxCount = max(maxCount, count)
    return maxCount

givenString = "blagdrahbhckc"
result = occurence(givenString)
print(result)