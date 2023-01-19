while True :
    user_action = input("Type add, show, complete or exit: ")
    user_action = user_action.strip()   #.strip removes spaces

    match user_action:
        case "add":
            todo = input("Enter a todo:") + "\n"    #"\n"   ---> add break line
            
            file = open("todos.txt", "r")           #"r"  --> read only         file = open(r"F:\Dev\Udemy\App1\todos.txt", "r")   --> 1st "r" is used to remove special characters
            todos = file.readlines()                #readlines = get everything in the file
            file.close()
            
            todos.append(todo)
            
            file = open('todos.txt', 'w')           #"w"  --> to write (overwrite)
            file.writelines(todos)                  #to write in the file
            file.close()
        
        case "show" | "display":                    # |   --> and
            file = open("todos.txt","r")            #get back previous list
            todos =  file.readlines()
            file.close()

            new_todos = [item.strip('\n') for item in todos]   #remove extra break line when print


            for index, item in enumerate(new_todos):    # enumerate --> function to list items 
                # item = item.strip("\n")      --> another solution remove break lines
                item = item.title()                 #title   --> capital letter on each wordud
                row = f"{index + 1}. {item}"        #f"{variable}aijiojoj{variable}"   -> remove spaces    "0 . Clean"  to "0.Clean"
                print(row)
        
        case "edit":
            number = int(input("Number of the todo to edit: "))          # int --> convert string to interger (input is always string value)
            number = number - 1
            new_todo = input("Enter a new todo:")
            todos[number] = new_todo

        case 'complete' :
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)                           #.pop   --> remove an item in a list // can use .remove
        
        case "exit":
            break
       
        case _:          #_     convention to say something else but can be repalce by a random variable liek "whatever" or "tootoot" or else
            print("Please enter a known comment")

print("Bye!")