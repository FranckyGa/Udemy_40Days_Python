#Experiment 1: get list of file and put filters
import glob

#get all files with .txt extension
myfile = glob.glob("06_files/*.txt")
print(myfile)

for filepath in myfile:
    with open(filepath, 'r') as file:
        print(file.read().upper())


#Experiment 2: read csv file and store data
import csv

with open("06_files/15_weather.csv","r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")
for row in data[1:]:
    if row[0] == city:
        print(row[1])


#Experiment 3: create a zip
import shutil

#shutil.make_archive("output", "zip", "06_files")   #06_files is the directory which contains files we want to zip

#Experiment 4:
import webbrowser
user_term = input("Enter a search term: ")
webbrowser.open("https://www.google.com/search?client=opera&q="  + user_term)


