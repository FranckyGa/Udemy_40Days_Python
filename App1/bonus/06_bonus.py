contents = ["Carrots are "
 "cooked",
 "The carrots were sliced.",
  "I didn't cut myself"]                        #Another way to create a list

filenames = ["doc.txt","report.txt","presentation"]

for content, filename in zip(contents, filenames):
    file = open(f"F:/Dev/Udemy/App1/06_files/{filename}", "w")            # will create a file if doesn't exist  ///  can also use : file = open(f"..06_files/{filename}", "w") 
    file.write(content)                                                   # ".."indicate to use the current path + the following

a = "I'm a string " \
    "by my own"                 #can use "\" to cut the text if we want to use one variable
print(a)