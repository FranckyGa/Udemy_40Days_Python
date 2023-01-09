password = input("Enter a password:\n")

result = {}         # {}  --> dictionary  => allow to associate a result to a name : ex : "high" 7

#Check 1 : password lenght
if len (password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

#Check 2 : digits
digit = False
for i in password:
    if i.isdigit():
        digit = True
result["Digit"] = digit

#Check 3 : uppercase
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["Uppercase"] = uppercase

print(result)

if all(result):             #  --->   same result than writting if all(result) == True:
    print("Strong password")
else:
    print("Weak password")