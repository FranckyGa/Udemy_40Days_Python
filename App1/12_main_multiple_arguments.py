#Read function
def get_todos(filepath):                               
    with open(filepath, "r") as file_local:        #Faster way to open and read file --> no need to close file
        todos_local = file_local.readlines()                #readlines = get everything in the file
    return todos_local

#Write procedure
def write_todos(filepath, todo_arg):
    with open(filepath, "w") as file:
        file.writelines(todo_arg)       #no return because nothing to return --> purpose is just to modify



while True :
    user_action = input("Type add, show, complete or exit: ")
    user_action = user_action.strip()   #.strip removes spaces

    
    if user_action.startswith("add") or user_action.startswith("new"):                        #we replaced "in" by ".startwith" more accurate in case of "edit add new member"
        todo = user_action[4:]

        todos = get_todos("todos.txt")                     #Function read file
        
        todos.append(todo + '\n')

        write_todos("todos.txt", todos)
    
    elif user_action.startswith("show"):                    
        todos = get_todos("todos.txt")

        new_todos = [item.strip('\n') for item in todos]   #remove extra break line when print

        for index, item in enumerate(new_todos):    # enumerate --> function to list items 
            # item = item.strip("\n")      --> another solution remove break lines
            item = item.title()                 #title   --> capital letter on each wordud
            row = f"{index + 1}. {item}"        #f"{variable}aijiojoj{variable}"   -> remove spaces    "0 . Clean"  to "0.Clean"
            print(row)
    
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])          # int --> convert string to interger (input is always string value)
            number = number - 1

            todos = get_todos("todos.txt")          #read file and get information

            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + '\n'         # \n   to add a break line like others

            write_todos("todos.txt", todos)         #write new todos on the file to existing todos
        
        #Manage error
        except ValueError:
            print("Your comment is not valid")
            continue                                        #To ignore what is following and start at the beginning

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
                
            todos = get_todos("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n')  #Remove break line
            todos.pop(index)                           #.pop   --> remove an item in a list // can use .remove
        
            write_todos("todos.txt", todos)

            message =  f"Todo {todo_to_remove} was temoved from the list."
            print(message)
        
        except IndexError:                                              #Manage errors
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    
    else:         
       print("Command not valid")

print("Bye!")