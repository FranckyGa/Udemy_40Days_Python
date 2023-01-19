#Erxercice 1 & 2:
try:
    total = float(input("Enter total value: "))
    myvalue = float(input("Enter a value: "))

    percent = (myvalue / total) *100
    print("That is ", percent, "%")

except ZeroDivisionError:
    print("You cannot divide by 0")

except:
    print("You need to enter a number. Run the program again")



