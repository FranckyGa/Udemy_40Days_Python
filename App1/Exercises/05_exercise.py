#Exercise 1:
filenames = ['document', 'report', 'presentation']

for index, name in enumerate(filenames):
    row = f"{index}-{name.capitalize()}.txt"
    print(row)

#Exercise 2:
ips = ['100.122.133.105', '100.122.133.111']

prompt_user = int(input("Enter a index: "))
print("You chose ", ips[prompt_user])