#exercise 1:
def convert(quantity):
    return float(quantity)/1000

my_conversion = input("Enter a liter to convert it into cubic meter : ")
result = convert(my_conversion)
print(result)

#exercise 2:
pwd = input("enter a password : ")

def test_pwd(password):
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
    
    if all(result.values()) == True:
        return "Your pwd is strong"
    else:
        return "Your pwd is weak"

r_test = test_pwd(pwd)

print(r_test)

    