def main():

    evens = [2, 4, 6, 8, 10]
    odds = [1, 3, 5, 7, 9]

    evenSquared = [ e**2 for e in evens if e > 4 and e < 8 ]
    print(evenSquared)

    evensDict = {e: e+10 for e in evens}
    print(evensDict)
    oddsDict = {e: e+10 for e in odds}
    print(oddsDict)

    numbers = {k:v for number in (evensDict, oddsDict) for k,v in number.items()}
    print(numbers)

if __name__ == "__main__":
    main()