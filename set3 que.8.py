i=1
while i<=5:
    num=int(input("enter the number"))
    if num==5:
        print(" wow you guessed currect number", 5)
    elif num<=5:
        print("less than equal",5)
    else:
        print("greater than ",5)
        i=i+1
    print()