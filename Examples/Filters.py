numbers = (1, 2, 3, 4, 5, 6, 7,  8, 0)
chars = "abcdefghIJKLMNOP"

def filterOdd(x):
    if x % 2 == 0:
        return x

def filterLower(x):
    if x.isupper():
        return False
    else:
        return True

def mapFilter(x):
    if (x >= 7):
        return "seven or more"
    elif (x >= 5 and x < 7):
        return "five to six"
    elif (x >= 3 and x < 5):
        return "three to four"
    return "less than three"

odds = list(filter(filterOdd, numbers))
print(odds)

lowers = list(filter(filterLower, chars))
print(lowers)

list3 = list(map(mapFilter, sorted(numbers)))
print(list3)