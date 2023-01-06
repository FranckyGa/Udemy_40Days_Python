#Exercise 1:
filename = "essay.txt"
file = open(f"F:/Dev/Udemy/App1/06_files/{filename}","r")
content = file.read()
print(content.title())

#Exercise 2:
print(len(content))

#Exercise 3:
filename = "members.txt"
file = open(f"F:/Dev/Udemy/App1/06_files/{filename}","r")
mylist = file.readlines()
file.close()

new_name = input("Please enter the new member name : ") +"\n"
mylist.append(new_name)

file = open(f"F:/Dev/Udemy/App1/06_files/{filename}","w")
file.writelines(mylist)
file.close()

#Exercise 4:
filename = ["doc1.txt","dox2.txt","doc3.txt"]
content = "hello"

for filenames in filename:
    file = open(f"F:/Dev/Udemy/App1/06_files/{filenames}","w")
    file.write(content)

#Exercise 5 :
filename = ["a.txt","b.txt","c.txt"]


for filenames in filename:
    file = open(f"F:/Dev/Udemy/App1/06_files/{filenames}","r")
    mylist = file.read()
    print(mylist)


