filenames = ["1.raw data.txt","2.Reports.txt", "3.presentation.txt"]

for filename in filenames:
    filename = filename.replace(".","-",1)          #1 at the end means number of occurence we want to change // optional
    print(filename)
print(filenames)


# Tuple : cannot modify a tuple --> .append doesn't work ; cannot replace something inside 
# filenames = ("1.raw data.txt","2.Reports.txt", "3.presentation.txt")