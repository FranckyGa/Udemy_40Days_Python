filenames = ["1.doc","2.documents","3.toto"]
filenames = [filename.replace(".","-") + ".txt" for filename in filenames]
print(filenames)