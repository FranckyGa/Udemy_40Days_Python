pwd = input("Enter a password :\n")
if len(pwd) > 7:
    print("Great password there")
elif len(pwd) == 7:
    print("Your password is ok but not too strong")
else:
    print("your password is weak")


