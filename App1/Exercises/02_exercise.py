text = input("write your name :")

print(text.capitalize())

#exercise 2:
x = 1
text2 = input("Write something :")
while x < 3:
    print(text2.capitalize())
    x = x + 1


#exercise 3:
x = 1
while x < 3:
    text3 = input("Write something :")
    print(text3.capitalize())
    x = x + 1


#How to find methods :
# dir(str)   --> will show all methods associated to strings
# dir( "aihiehi")   --> can also work
# dir(list)

help(str.capitalize)  # help to understand the function