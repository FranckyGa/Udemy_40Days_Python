def get_average():
    with open("06_files/data.txt","r") as file:
        data = file.readlines()        
    
    values = data[1:]           #Sliced : Remove the 1st item of the list (i.e temperature)
    values = [float(i) for i in values]     #transform list in list of numbers
    
    average_local = sum(values)/len(values)
    return average_local



average = get_average()
print(average)