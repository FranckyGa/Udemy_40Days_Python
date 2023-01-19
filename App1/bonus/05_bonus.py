waiting_list = ["sen", "ben", "john"]
waiting_list.sort()                         #.sort   --> sort the list defined above
#waiting_list.sort(reverse=True)            #inverte the list (Z to A)

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)