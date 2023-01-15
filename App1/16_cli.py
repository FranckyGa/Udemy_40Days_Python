#from function import write_todos, get_todos           #import file with functions but have to name all functions we want to use
from Modules import functions         #--> can use this synthax but need call it before : function.write_todos    otherwise won't work
                                      #from Modules    --> indicates where is the file we want to impôrt if not in the same field than the main code
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True :
    user_action = input("Type add, show, complete or exit: ")
    user_action = user_action.strip()                  #.strip removes spaces

    
    if user_action.startswith("add") or user_action.startswith("new"):             #we replaced "in" by ".startwith" more accurate in case of "edit add new member"
        todo = user_action[4:]

        todos = functions.get_todos()                            #Function read file (we use default argument)
        
        todos.append(todo + '\n')

        functions.write_todos(todos)                             #if want to enter all arg can be : function.(filepath = "todos.txt", todo_arg = todos)   --> order doesn't matter in this case cause we named them
    
    elif user_action.startswith("show"):                    
        todos = functions.get_todos()

        new_todos = [item.strip('\n') for item in todos]   #remove extra break line when print

        for index, item in enumerate(new_todos):    # enumerate --> function to list items 
            # item = item.strip("\n")      --> another solution remove break lines
            item = item.title()                     #title   --> capital letter on each wordud
            row = f"{index + 1}. {item}"            #f"{variable}aijiojoj{variable}"   -> remove spaces    "0 . Clean"  to "0.Clean"
            print(row)
    
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])          # int --> convert string to interger (input is always string value)
            number = number - 1

            todos = functions.get_todos()                    #read file and get information

            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + '\n'        # \n   to add a break line like others

            function.write_todos(todos)                     #write new todos on the file to existing todos
        
        #Manage error
        except ValueError:
            print("Your comment is not valid")
            continue                               #To ignore what is following and start at the beginning

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
                
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')  #Remove break line
            todos.pop(index)                           #.pop   --> remove an item in a list // can use .remove
        
            functions.write_todos(todos)

            message =  f"Todo {todo_to_remove} was temoved from the list."
            print(message)
        
        except IndexError:                            #Manage errors
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    
    else:         
       print("Command not valid")

print("Bye!")