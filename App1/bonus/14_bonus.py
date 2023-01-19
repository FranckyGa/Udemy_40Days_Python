from Modules import bonus_function

feet_inches = input("Enter feet and inches: ")

parsed = bonus_function.parse(feet_inches)
result = bonus_function.convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters.")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")


