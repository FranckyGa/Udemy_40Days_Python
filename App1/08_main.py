while True :
    user_action = input("Type add, show, complete or exit: ")
    user_action = user_action.strip()   #.strip removes spaces

    match user_action:
        case "add":
            todo = input("Enter a todo:") + "\n"    #"\n"   ---> add break line

            with open("todos.txt", "r") as file:        #Faster way to open and read file --> no need to close file
                todos = file.readlines()                #readlines = get everything in the file
            
            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        
        case "show" | "display":                    # |   --> and
            with open("todos.txt","r") as file:           #get back previous list
                todos =  file.readlines()

            new_todos = [item.strip('\n') for item in todos]   #remove extra break line when print

            for index, item in enumerate(new_todos):    # enumerate --> function to list items 
                # item = item.strip("\n")      --> another solution remove break lines
                item = item.title()                 #title   --> capital letter on each wordud
                row = f"{index + 1}. {item}"        #f"{variable}aijiojoj{variable}"   -> remove spaces    "0 . Clean"  to "0.Clean"
                print(row)
        
        case "edit":
            number = int(input("Number of the todo to edit: "))          # int --> convert string to interger (input is always string value)
            number = number - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + '\n'                     # \n   to add a break line like others

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete' :
            number = int(input("Number of the todo to complete: "))
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')  #Remove break line
            todos.pop(index)                           #.pop   --> remove an item in a list // can use .remove
        
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message =  f"Todo {todo_to_remove} was temoved from the list."
            print(message)

        case "exit":
            break
       
        case _:          #_     convention to say something else but can be repalce by a random variable liek "whatever" or "tootoot" or else
            print("Please enter a known comment")

print("Bye!")