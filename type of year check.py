year = int(input("Enter a year: "))

if year<1582:
    print("Not with in the gregorian period")
else:
    if year%4!=0:
        print("Common year")
    elif year%100!=0:
        print("Leap year")
    elif year%400!=0:
        print("Common year")
    else:
        print("Leap year")